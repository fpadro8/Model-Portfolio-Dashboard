import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

API_KEY = os.getenv("CLAUDE_API_KEY")
MODEL = os.getenv("CLAUDE_MODEL", "claude-haiku-4-5-20251001")

class ClaudeError(Exception):
    pass

def generate(prompt: str, max_tokens: int = 512, temperature: float = 0.0, timeout: int = 30) -> str:
    if not API_KEY:
        raise ClaudeError("CLAUDE_API_KEY not set in environment")

    client = anthropic.Anthropic(api_key=API_KEY)

    try:
        resp = client.messages.create(
            model=MODEL,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
        )
    except Exception as exc:
        raise ClaudeError(f"Anthropic SDK request failed: {exc}") from exc

    return resp.content[0].text


if __name__ == "__main__":
    prompt = "Write a short haiku about programming in Python."
    print("Using model:", MODEL)
    try:
        out = generate(prompt, max_tokens=120)
        print("--- completion ---")
        print(out)
    except ClaudeError as e:
        print("Error:", e)
