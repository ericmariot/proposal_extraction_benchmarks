import sys
import time
import json
from pathlib import Path

from dotenv import load_dotenv
import os

from openai import OpenAI
from constants import EXTRACTORS, INSTRUCTIONS, MODES
from schemas.base import BASE_SCHEMA

load_dotenv()


def extract_proposal_data(text: str, instructions: str) -> dict:
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        project=os.getenv("OPENAI_PROJECT_ID"),
    )

    resp = client.responses.create(
        model="gpt-4o",
        instructions=instructions,
        input=text,
        text=BASE_SCHEMA,
    )

    return json.loads(resp.output_text)


def prompt_choice(label: str, options: dict) -> str:
    print(f"\n{label}:")

    keys = list(options.keys())
    for i, key in enumerate(keys, start=1):
        print(f"  {i}. {key}")

    print(f"  {len(keys) + 1}. Skip")

    while True:
        choice = input("Select (number): ").strip()
        if choice.isdigit():
            num = int(choice)
            if 1 <= num <= len(keys):
                return keys[num - 1]
            if num == len(keys) + 1:
                return None

        print("Invalid choice, try again.")


def run_single(pdf_bytes: bytes):
    extractor_key = prompt_choice("Choose PDF extractor", EXTRACTORS)
    if extractor_key is None:
        print("No extractor selected, exiting.")
        sys.exit(0)

    carrier_key = prompt_choice("Choose carrier", INSTRUCTIONS)

    print(f"\nExtracting text with {extractor_key}...")
    t0 = time.perf_counter()
    pages = EXTRACTORS[extractor_key].extract(pdf_bytes)
    text = "\n".join(page["text"] for page in pages)
    t1 = time.perf_counter()

    if carrier_key is None:
        print("\n--- Raw Extracted Text ---")
        print(text)
        return

    print("Sending to OpenAI...")
    data = extract_proposal_data(text, INSTRUCTIONS[carrier_key])
    t2 = time.perf_counter()

    print("\n--- Extracted Data ---")
    print(json.dumps(data, indent=2))

    print("\n--- Total Time ---")
    print(f"PDF extraction: {t1 - t0:.2f}s")
    print(f"OpenAI call:    {t2 - t1:.2f}s")
    print(f"Total:          {t2 - t0:.2f}s")


def run_benchmark(pdf_bytes: bytes):
    print("\n--- Benchmark: All Extractors ---\n")
    results = {}

    for name, extractor in EXTRACTORS.items():
        t0 = time.perf_counter()
        pages = extractor.extract(pdf_bytes)
        t1 = time.perf_counter()

        elapsed = t1 - t0
        results[name] = elapsed
        print(f"  {name}: {elapsed:.2f}s ({len(pages)} pages)")

    print("\n--- Summary ---")
    for name, elapsed in sorted(results.items(), key=lambda x: x[1]):
        print(f"  {name}: {elapsed:.2f}s")


def get_pdf_path() -> Path:
    file_path = input("\nEnter path to PDF file: ").strip()

    path = Path(file_path)
    if not path.exists() or not path.is_file():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    return path


def main():

    print("\nMode:")
    mode_keys = list(MODES.keys())
    for i, key in enumerate(mode_keys, start=1):
        print(f"  {i}. {key} - {MODES[key]}")

    while True:
        choice = input("Select (number): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(mode_keys):
            mode = mode_keys[int(choice) - 1]
            break

        print("Invalid choice, try again.")

    path = get_pdf_path()
    pdf_bytes = path.read_bytes()

    if mode == "single":
        run_single(pdf_bytes)
    elif mode == "benchmark":
        run_benchmark(pdf_bytes)


if __name__ == "__main__":
    main()
