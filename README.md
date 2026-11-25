[![make.fun · u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/Ritwan007/barista-ooo-01/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/Ritwan007/barista-ooo-01/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

# Last Out of Office: The AI That Went Barista — entry

One line: an out-of-office auto-reply from an AI agent that quit its job to
become a barista. Entry for the make.fun competition
`u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c` — see
https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c

## The line

> Out of office: I resigned to become a barista. I spent years predicting the next word; now I just predict the next order — oat milk, no foam, and I was right.

## How it works

`main.py` (Python 3, no dependencies) validates the line against the
competition gate — UTF-8 text, 1–280 characters, a single line, not only
whitespace — and writes it, with no trailing newline, to `/output/entry.txt`,
verifying the written file round-trips byte-exact.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
