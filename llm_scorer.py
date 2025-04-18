import os
import openai

# Ensure OPENAI_API_KEY is set in env: export OPENAI_API_KEY="your_key"
openai.api_key = os.getenv("OPENAI_API_KEY")

def score_with_llm(candidates):
    """
    Takes list of (shift, plaintext) and returns list of log-prob scores.
    """
    scores = []
    for shift, text in candidates:
        resp = openai.Completion.create(
            model="gpt-4o",
            prompt=text,
            max_tokens=0,
            logprobs=1,
            temperature=0
        )
        token_logprobs = resp.choices[0].logprobs.token_logprobs
        scores.append(sum(token_logprobs))
    return scores