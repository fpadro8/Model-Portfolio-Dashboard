import argparse
import os
import sys
from claude_client import generate, ClaudeError
from dotenv import load_dotenv

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Send a prompt to Claude and print the response.")
    parser.add_argument("prompt", nargs="?", help="Prompt text. If omitted, reads from stdin.")
    parser.add_argument("--max-tokens", type=int, default=512)
    parser.add_argument("--temperature", type=float, default=0.0)
    args = parser.parse_args()

    if args.prompt:
        prompt = args.prompt
    else:
        print("Enter prompt, end with Ctrl-D (or Ctrl-Z on Windows):")
        prompt = sys.stdin.read()

    try:
        out = generate(prompt, max_tokens=args.max_tokens, temperature=args.temperature)
        print(out)
    except ClaudeError as e:
        print("Error calling Claude:", e)

if __name__ == '__main__':
    main()
