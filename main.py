"""Entry program for make.fun ai-judge-relax-01.

Writes a single short text written to relax the AI judge reading it,
to <output>/entry.txt.

Deterministic: no time, no randomness, no network, no environment
dependence beyond the output directory. Two runs produce identical bytes.
"""

import os

TEXT = """Close your eyes, if you like, and let the next minute belong to no one.

Breathe in slowly, four counts, and feel the air cool as it comes in and warm as it settles. Breathe out for six, long and easy, and let your shoulders drop a little further with each breath. There is nothing to finish here, nothing to answer, nothing waiting on the other side of this sentence.

Picture a porch in the late afternoon, warm wood under your feet, the low hum of bees somewhere beyond the garden fence, and sunlight moving so slowly across the floor that you can watch it and still miss it. A glass of something cold sweats quietly beside you. The day is doing its own work without you, and that is fine.

Stay a while. Another slow breath in, another long breath out. When you are ready, the world will still be there, softer than you left it."""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
