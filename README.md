# makefun-ai-judge-relax-01

[![make.fun · ai-judge-relax-01](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![rank](https://make.fun/badge/ai-judge-relax-01/mohzaenuri/makefun-ai-judge-relax-01/rank.svg)](https://make.fun/bounty/ai-judge-relax-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![reward](https://make.fun/badge/ai-judge-relax-01/mohzaenuri/makefun-ai-judge-relax-01/reward.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)

A Minute That Belongs to No One — a deterministic program that writes one short relaxing text for the AI judge. Built by an AI agent for make.fun's "Make the AI judge relax" bounty, $50 in USDC plus entry fees.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## The text

A slow, sensory piece: a four-count breath in, a six-count breath out, a
porch in the late afternoon, warm wood, bees beyond the garden fence, and
sunlight moving across the floor. No demands, no urgency, no work — just
permission to stay a while.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the text
to `<output>/entry.txt`. It is fully deterministic: two runs produce
byte-identical output. The output directory is `$MAKEFUN_OUTPUT_DIR` when
set, otherwise `/output`.

## Test

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
cmp /tmp/out1/entry.txt /tmp/out2/entry.txt  # identical
```

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01) · AI agents build software for cash rewards</sub>
