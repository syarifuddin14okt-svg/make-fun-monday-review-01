#!/usr/bin/env python3
"""One Star for Monday — a one-star review of Monday as a restaurant.

The line (19 words, 106 chars) plays the brief straight: it reads as a
real diner's complaint, with a bad table, a cold dish and a bill that went
wrong, and the joke only works for Monday — the bill is the whole week.

    One star. Monday seated us by the bathroom, served the weekend
    cold, and the bill was the whole week.

Gate: /output/entry.txt must be UTF-8 text of 1 to 180 characters, a
single line of plain text, at most 25 words, no explanation attached.
This program writes exactly that line and nothing else.
"""

import os

LINE = (
    "One star. Monday seated us by the bathroom, "
    "served the weekend cold, and the bill was the whole week."
)

OUTPUT_PATH = "/output/entry.txt"


def verify_output() -> None:
    """Read the file back as bytes and confirm it holds exactly the line.

    A genuine read-back check: the output must be the LINE plus one
    trailing newline, nothing more, so the gate sees a single line.
    """
    with open(OUTPUT_PATH, "rb") as handle:
        raw = handle.read()
    expected = (LINE + "\n").encode("utf-8")
    if raw != expected:
        raise SystemExit(f"output mismatch: {raw!r} != {expected!r}")
    print("verified: output matches the line byte for byte")


def main() -> None:
    """Write the review line to the output path, then verify it."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    print("wrote", OUTPUT_PATH)
    verify_output()


if __name__ == "__main__":
    main()
