FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ai_ml_ops/ ai_ml_ops/
COPY deploy/ deploy/
COPY datasets/ datasets/

ENV PYTHONPATH=/app

EXPOSE 8000

# Override RUN_ID at deploy time:
# docker run -e RUN_ID=abc123 ai-ml-ops-serve:latest
ENV RUN_ID=""
CMD ["sh", "-c", "python ai_ml_ops/serve.py --run_id ${RUN_ID}"]
