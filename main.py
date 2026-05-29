"""Dry-run: load .env and verify Gemini, Groq, and OpenAI API keys."""

import os
import sys

from dotenv import load_dotenv


def mask(value: str | None) -> str:
    if not value:
        return "(missing)"
    if len(value) <= 8:
        return "***"
    return f"{value[:4]}...{value[-4:]}"


def check_env() -> bool:
    load_dotenv()
    google_key = os.getenv("GOOGLE_API_KEY")
    groq_key = os.getenv("GROQ_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")

    print("=== Dry run: environment ===")
    print(f"GOOGLE_API_KEY:  {mask(google_key)}")
    print(f"GROQ_API_KEY:    {mask(groq_key)}")
    print(f"OPENAI_API_KEY:  {mask(openai_key)}")

    ok = True
    if not google_key:
        print("FAIL: GOOGLE_API_KEY not set")
        ok = False
    if not groq_key:
        print("FAIL: GROQ_API_KEY not set")
        ok = False
    if not openai_key:
        print("FAIL: OPENAI_API_KEY not set")
        ok = False
    return ok


def ping_google() -> None:
    from langchain_google_genai import ChatGoogleGenerativeAI

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", max_tokens=16)
    reply = llm.invoke("Reply with exactly: ok")
    print(f"Gemini: {reply.content.strip()}")


def ping_groq() -> None:
    from langchain_groq import ChatGroq

    llm = ChatGroq(model="llama-3.1-8b-instant", max_tokens=16)
    reply = llm.invoke("Reply with exactly: ok")
    print(f"Groq:   {reply.content.strip()}")


def main() -> None:
    if not check_env():
        sys.exit(1)

    print("\n=== Dry run: API connectivity (minimal call) ===")
    results: list[bool] = []

    try:
        ping_google()
        results.append(True)
    except Exception as e:
        err = str(e)
        if "429" in err or "RESOURCE_EXHAUSTED" in err or "quota" in err.lower():
            print("Gemini: key loaded OK, but quota/rate limit hit (not an auth error)")
            results.append(True)
        else:
            print(f"Gemini FAIL: {e}")
            results.append(False)

    try:
        ping_groq()
        results.append(True)
    except Exception as e:
        print(f"Groq FAIL: {e}")
        results.append(False)

    if all(results):
        print("\nDry run passed.")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
