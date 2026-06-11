"""RAG pipeline over ML project corpus — AIOps Week 9."""

import json
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd
import typer
from typing_extensions import Annotated

from madewithml.aiops.guards import check_input, check_output, refusal_message

app = typer.Typer()
PROMPT_PATH = Path(__file__).parent / "prompts" / "rag_system.txt"


def load_prompt_template() -> str:
    return PROMPT_PATH.read_text()


def load_corpus(corpus_path: str) -> pd.DataFrame:
    df = pd.read_csv(corpus_path)
    text_col = "description" if "description" in df.columns else df.columns[-1]
    title_col = "title" if "title" in df.columns else df.columns[0]
    df["document"] = df[title_col].astype(str) + "\n" + df[text_col].astype(str)
    df["title"] = df[title_col].astype(str)
    return df


def build_index(corpus_path: str, index_dir: str) -> None:
    """Build Chroma vector index from a CSV corpus."""
    from llama_index.core import Document, Settings, VectorStoreIndex
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding
    from llama_index.vector_stores.chroma import ChromaVectorStore
    import chromadb

    df = load_corpus(corpus_path)
    documents = [Document(text=row.document, metadata={"title": row.title}) for row in df.itertuples()]

    Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

    index_path = Path(index_dir)
    index_path.mkdir(parents=True, exist_ok=True)
    chroma_client = chromadb.PersistentClient(path=str(index_path))
    chroma_collection = chroma_client.get_or_create_collection("ml_projects")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    VectorStoreIndex.from_documents(documents, vector_store=vector_store)

    typer.echo(f"Index built at {index_dir} with {len(documents)} documents.")


def load_index(index_dir: str):
    from llama_index.core import Settings, StorageContext, load_index_from_storage
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding
    from llama_index.vector_stores.chroma import ChromaVectorStore
    import chromadb

    Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
    chroma_client = chromadb.PersistentClient(path=index_dir)
    chroma_collection = chroma_client.get_or_create_collection("ml_projects")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    return load_index_from_storage(storage_context)


def retrieve_context(index, question: str, top_k: int = 3) -> tuple[str, List[Dict[str, Any]]]:
    retriever = index.as_retriever(similarity_top_k=top_k)
    nodes = retriever.retrieve(question)
    chunks = []
    for node in nodes:
        chunks.append(
            {
                "title": node.metadata.get("title", "unknown"),
                "score": round(float(node.score or 0.0), 4),
                "text": node.text[:300],
            }
        )
    context = "\n\n".join(f"[{c['title']}] {c['text']}" for c in chunks)
    return context, chunks


def generate_answer(question: str, context: str, model: str) -> str:
    from llama_index.llms.ollama import Ollama

    template = load_prompt_template()
    prompt = template.format(context=context or "No context available.", question=question)
    llm = Ollama(model=model, request_timeout=120.0)
    response = llm.complete(prompt)
    return str(response).strip()


def maybe_trace(question: str, answer: str, sources: List[Dict], latency_ms: float, enabled: bool) -> None:
    if not enabled:
        return
    try:
        from langfuse import Langfuse

        langfuse = Langfuse()
        trace = langfuse.trace(name="rag-ask", input={"question": question})
        trace.span(name="retrieval", output={"sources": sources})
        trace.generation(name="llm", output=answer, metadata={"latency_ms": latency_ms})
        langfuse.flush()
    except Exception as exc:
        typer.echo(f"Langfuse trace skipped: {exc}")


def ask(
    question: str,
    index_dir: str,
    model: str = "llama3.2:1b",
    top_k: int = 3,
    no_retrieval: bool = False,
    trace: bool = False,
) -> Dict[str, Any]:
    input_guard = check_input(question)
    if not input_guard.allowed:
        return {
            "answer": refusal_message(input_guard.reason),
            "sources": [],
            "latency_ms": 0,
            "guardrail_triggered": True,
            "guardrail_reason": input_guard.reason,
        }

    start = time.perf_counter()
    index = load_index(index_dir) if not no_retrieval else None
    context, sources = ("", [])
    if index:
        context, sources = retrieve_context(index, question, top_k=top_k)

    answer = generate_answer(question, context, model=model)
    latency_ms = round((time.perf_counter() - start) * 1000, 1)

    output_guard = check_output(answer, context_provided=bool(context))
    if not output_guard.allowed:
        result = {
            "answer": refusal_message(output_guard.reason),
            "sources": sources,
            "latency_ms": latency_ms,
            "guardrail_triggered": True,
            "guardrail_reason": output_guard.reason,
        }
    else:
        result = {
            "answer": answer,
            "sources": sources,
            "latency_ms": latency_ms,
            "guardrail_triggered": False,
        }

    maybe_trace(question, result["answer"], sources, latency_ms, enabled=trace)
    return result


@app.command()
def build_index_cmd(
    corpus: Annotated[str, typer.Option("--corpus")] = "datasets/projects.csv",
    index_dir: Annotated[str, typer.Option("--index-dir")] = "results/rag_index",
) -> None:
    """Build vector index from corpus CSV."""
    build_index(corpus, index_dir)


@app.command()
def inspect_index(
    index_dir: Annotated[str, typer.Option("--index-dir")] = "results/rag_index",
) -> None:
    """Print document count in the index."""
    import chromadb

    client = chromadb.PersistentClient(path=index_dir)
    collection = client.get_or_create_collection("ml_projects")
    typer.echo(json.dumps({"index_dir": index_dir, "document_count": collection.count()}, indent=2))


@app.command()
def ask_cmd(
    question: Annotated[str, typer.Option("--question")],
    index_dir: Annotated[str, typer.Option("--index-dir")] = "results/rag_index",
    model: Annotated[str, typer.Option("--model")] = "llama3.2:1b",
    top_k: Annotated[int, typer.Option("--top-k")] = 3,
    no_retrieval: Annotated[bool, typer.Option("--no-retrieval")] = False,
    trace: Annotated[bool, typer.Option("--trace")] = False,
) -> None:
    """Ask a question using RAG."""
    result = ask(
        question=question,
        index_dir=index_dir,
        model=model,
        top_k=top_k,
        no_retrieval=no_retrieval,
        trace=trace,
    )
    typer.echo(json.dumps(result, indent=2))


if __name__ == "__main__":
    app()
