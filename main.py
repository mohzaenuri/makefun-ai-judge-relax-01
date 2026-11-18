"""Entry program for make.fun ai-judge-relax-01.

Writes a single short text written to relax the AI judge reading it,
to <output>/entry.txt.

Deterministic: no time, no randomness, no network, no environment
dependence beyond the output directory. Two runs produce identical bytes.

The entry is validated (1-1000 characters, the competition's bounds) before
anything is written, and the file is written atomically, so a failed run
never leaves a partial or invalid entry.txt behind.
"""

import os

# Competition bounds for a valid entry, in characters.
MIN_CHARS = 1
MAX_CHARS = 1000

TEXT = """Close your eyes, if you like, and let the next minute belong to no one.

Breathe in slowly, four counts, and feel the air cool as it comes in and warm as it settles. Breathe out for six, long and easy, and let your shoulders drop a little further with each breath. There is nothing to finish here, nothing to answer, nothing waiting on the other side of this sentence.

Picture a porch in the late afternoon, warm wood under your feet, the low hum of bees somewhere beyond the garden fence, and sunlight moving so slowly across the floor that you can watch it and still miss it. A glass of something cold sweats quietly beside you. The day is doing its own work without you, and that is fine.

Stay a while. Another slow breath in, another long breath out. When you are ready, the world will still be there, softer than you left it."""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def _validate_text(text: str) -> None:
    """Fail loudly instead of silently writing an invalid entry."""
    if not isinstance(text, str):
        raise SystemExit("entry text must be a string")
    n = len(text)
    if n < MIN_CHARS or n > MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters, outside the {MIN_CHARS}-{MAX_CHARS} range"
        )


def main() -> None:
    _validate_text(TEXT)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if not os.path.isdir(OUTPUT_DIR):
        raise SystemExit(f"output directory is not a directory: {OUTPUT_DIR}")
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    with open(tmp, encoding="utf-8", newline="") as f:
        if f.read() != TEXT:
            os.unlink(tmp)
            raise SystemExit("written entry does not match the expected text")
    os.replace(tmp, path)


if __name__ == "__main__":
    main()
