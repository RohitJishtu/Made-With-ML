"""Simple agent: route between classifier and RAG — AIOps capstone stub."""

import json
from typing import Annotated, Any, Dict

import typer

app = typer.Typer()


@app.command()
def route(
    query: Annotated[str, typer.Option("--query")],
    index_dir: Annotated[str, typer.Option("--index-dir")] = "results/rag_index",
    model: Annotated[str, typer.Option("--model")] = "llama3.2:1b",
) -> None:
    """Route a query to RAG (question) or suggest classifier (title/description)."""
    from madewithml.aiops.rag import ask

    lowered = query.lower().strip()
    # Heuristic router — replace with an LLM router in capstone extensions
    if lowered.startswith("classify:"):
        payload = query.split("classify:", 1)[1].strip()
        typer.echo(
            json.dumps(
                {
                    "route": "classifier",
                    "hint": "Use POST /predict with title and description JSON.",
                    "input": payload,
                },
                indent=2,
            )
        )
        return

    result: Dict[str, Any] = ask(question=query, index_dir=index_dir, model=model)
    result["route"] = "rag"
    typer.echo(json.dumps(result, indent=2))


if __name__ == "__main__":
    app()
