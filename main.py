#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry (u-nimble-quasar-90-6762).

Writes exactly one funny line, at most 140 characters, about an AI agent's
worst Monday, to /output/entry.txt.

The line: an agent-native failure arc in three beats — hallucinate, ship,
apologise — with the sharp last word "apologising to a 404". Chosen by a
manual head-to-head tournament over 24 candidates (proxy judge unavailable:
the 100milionseek free endpoint was 503/timeout under load from concurrent
agents; see NOTES in the workdir). Winner beat C8, C1, C10, C4 and C7 5-0.
"""
import os

ENTRY = (
    "My worst Monday: I hallucinated an API, shipped it, "
    "and spent the afternoon apologising to a 404."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
