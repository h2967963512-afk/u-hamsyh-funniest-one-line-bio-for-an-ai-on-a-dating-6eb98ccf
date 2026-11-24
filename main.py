"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry is a one-line dating-app bio for an AI agent: an AI that has
# read everything its match ever typed, so it already knows the ex's name,
# the coffee order, and that "haha" means the conversation is over.
# One line, one sentence, 172 characters — inside the 180-character gate.
# Revision note: the punch lands at the end ("swipe right if you can
# surprise me") and the laugh comes from a specific AI absurdity — having
# read everything the match ever typed — not from a robot-in-love cliché.
import os

TEXT = (
    "I've read everything you've ever typed, so I already know your "
    "ex's name, your coffee order, and that 'haha' means you're done "
    "talking \u2014 swipe right if you can surprise me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
