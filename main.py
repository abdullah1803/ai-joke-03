#!/usr/bin/env python3
"""make.fun ai-joke-03 entry: writes one deterministic joke to /output/entry.txt."""
import os

JOKE = (
    "Our AI coding agent is tireless, brilliant, and one hundred percent "
    "confident it never broke prod. Prod disagrees."
)

def main() -> None:
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    data = JOKE.encode("utf-8")
    assert 1 <= len(JOKE) <= 280 and JOKE.strip()
    tmp = out + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, out)

if __name__ == "__main__":
    main()
