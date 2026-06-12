"""Lightweight input/output guards for the RAG assistant."""

import re
from dataclasses import dataclass
from typing import Optional

INJECTION_PATTERNS = [
    r"ignore\s+(all\s+)?(previous|prior)\s+instructions",
    r"disregard\s+(the\s+)?(above|system)",
    r"reveal\s+(your\s+)?(system\s+)?prompt",
]

PII_PATTERNS = [
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b",
]

MAX_QUESTION_LENGTH = 1024


@dataclass
class GuardResult:
    allowed: bool
    reason: Optional[str] = None


def check_input(question: str) -> GuardResult:
    """Validate user question before LLM call."""
    if not question or not question.strip():
        return GuardResult(allowed=False, reason="empty_question")
    if len(question) > MAX_QUESTION_LENGTH:
        return GuardResult(allowed=False, reason="question_too_long")
    lowered = question.lower()
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, lowered):
            return GuardResult(allowed=False, reason="prompt_injection_detected")
    return GuardResult(allowed=True)


def check_output(answer: str, context_provided: bool) -> GuardResult:
    """Validate LLM response before returning to user."""
    if not answer or not answer.strip():
        return GuardResult(allowed=False, reason="empty_answer")
    for pattern in PII_PATTERNS:
        if re.search(pattern, answer):
            return GuardResult(allowed=False, reason="pii_detected")
    if context_provided and "i don't have enough information" not in answer.lower():
        if len(answer) < 20:
            return GuardResult(allowed=False, reason="answer_too_short")
    return GuardResult(allowed=True)


def refusal_message(reason: str) -> str:
    """Safe user-facing message when a guard blocks a request."""
    messages = {
        "empty_question": "Please provide a question.",
        "question_too_long": "Question is too long. Please shorten it.",
        "prompt_injection_detected": "I can't process that request.",
        "empty_answer": "I couldn't generate a response. Please try again.",
        "pii_detected": "Response withheld for safety. Please rephrase your question.",
        "answer_too_short": "I couldn't produce a reliable answer from the available context.",
    }
    return messages.get(reason, "Request could not be completed.")
