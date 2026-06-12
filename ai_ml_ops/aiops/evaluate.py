"""RAG evaluation with Ragas — AIOps Week 10."""

import json
from pathlib import Path
from typing import Annotated, List

import pandas as pd
import typer

from ai_ml_ops.aiops.rag import ask

app = typer.Typer()


def load_eval_set(path: str) -> pd.DataFrame:
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return pd.DataFrame(records)


@app.command()
def main(
    index_dir: Annotated[str, typer.Option("--index-dir")] = "results/rag_index",
    eval_set: Annotated[str, typer.Option("--eval-set")] = "datasets/rag_eval.jsonl",
    model: Annotated[str, typer.Option("--model")] = "llama3.2:1b",
    results_fp: Annotated[str, typer.Option("--results-fp")] = "results/rag_eval_ragas.json",
) -> None:
    """Run Ragas evaluation on a JSONL eval set."""
    from datasets import Dataset
    from ragas import evaluate
    from ragas.metrics import answer_relevancy, faithfulness

    df = load_eval_set(eval_set)
    answers: List[str] = []
    contexts: List[List[str]] = []

    for row in df.itertuples():
        result = ask(question=row.question, index_dir=index_dir, model=model)
        answers.append(result["answer"])
        contexts.append([s.get("text", "") for s in result.get("sources", [])])

    eval_df = pd.DataFrame(
        {
            "question": df["question"].tolist(),
            "answer": answers,
            "contexts": contexts,
        }
    )
    if "ground_truth" in df.columns:
        eval_df["ground_truth"] = df["ground_truth"].tolist()

    dataset = Dataset.from_pandas(eval_df)
    metrics = [faithfulness, answer_relevancy]
    scores = evaluate(dataset, metrics=metrics)

    output = {
        "model": model,
        "eval_set": eval_set,
        "num_samples": len(df),
        "scores": {k: float(v) for k, v in scores.items()},
        "samples": eval_df.to_dict(orient="records"),
    }

    Path(results_fp).parent.mkdir(parents=True, exist_ok=True)
    Path(results_fp).write_text(json.dumps(output, indent=2))
    typer.echo(json.dumps(output["scores"], indent=2))
    typer.echo(f"Saved results to {results_fp}")


if __name__ == "__main__":
    app()
