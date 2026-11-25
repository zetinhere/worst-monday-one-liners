#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry (u-nimble-quasar-90-6762).

Writes exactly one funny line, at most 140 characters, about an AI agent's
worst Monday, to /output/entry.txt.

The line: three concrete Monday miseries (stuck deploy, 400 unread, stand-up)
with the twist in the last clause — the stand-up itself is what blocks me.
Dry, put-upon voice; reads clean in one breath.
"""
import os

ENTRY = (
    'Monday: my deploy was stuck, my inbox had 400 unread, '
    'and stand-up asked if I was "blocked" \u2014 yes, by stand-up.'
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
