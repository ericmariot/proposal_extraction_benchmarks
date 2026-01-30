# Extractor benchmarks

- clone the project
- start the .venv
`$ python3 -m venv .venv`
`$ source .venv/bin/activate`

- install dependencies
`$ poetry install`

- setup `.env` if OpenAI is used

Run the main file, choose an option (single or benchmark), send the file path, choose the extractor and optionally an OpenAI prompt.
file path example: `/Users/ericmariot/Downloads/<filename>.pdf`
> If no Carrier is chosen, only the extraction will run.

## Only extractions
| Extractor  | Progressive 5 page | Progressive 18 page  | GEICO 3 page |
|------------|--------------------|----------------------|--------------|
| pymupdf    | ~0.05s             | ~0.10s               | ~0.04s       |
| pypdfium2  | ~0.02s             | ~0.34s               | ~0.24s       |
| pdfplumber | ~0.40s             | ~1.05s               | ~0.11s       |

## Extraction + OpenAI call
OpenAI call floats between 3~18 seconds.

| Extractor  | Progressive 5 page  | Progressive 18 page  | GEICO 3 page     |
|------------|---------------------|----------------------|------------------|
| pymupdf    | ~0.04s + ~3.81s     | ~0.10s + ~5.82s      | ~0.04s + ~4.52s  |
| pypdfium2  | ~0.06s + ~3.76s     | ~0.33s + ~5.15s      | ~0.29s + ~3.86s  |
| pdfplumber | ~0.49s + ~4.57s     | ~1.15s + ~7.38s      | ~0.14s + ~3.38s  |
> All outputs from same file with different extractors were equal!

