#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue to /output/entry.txt. The monologue is spoken by
Malachar, a dark lord, to the hero who has come to kill him. He never
says he is tired: the tiredness lives in the pauses, the broken chair,
the two hundred stairs, the tea going cold, and the sentence he cannot
quite finish.
"""

import os

MONOLOGUE = (
    "Sit down, hero, and listen. Not that chair \u2014 the leg's gone. There. "
    "Now. You've come to kill me, yes? Sword, destiny, the whole bright "
    "shining parade. I've buried thirty of you. Thirty-one. The bards never "
    "mention the stairs. Two hundred of them, hero, and my knees \u2014 well. "
    "The point is this: the wells of Aldermere turn black at the thaw, the "
    "ravens already carry my letters, and your little rebellion ends when "
    "the snow does. So drink your tea before it cools. Dawn comes early "
    "and hungry. Bring your best sword. I'll bring \u2014 whatever's left "
    "of Malachar."
)


def main() -> None:
    words = MONOLOGUE.split()
    if not 90 <= len(words) <= 110:
        raise SystemExit(f"monologue is {len(words)} words, expected about 100")
    if not 1 <= len(MONOLOGUE) <= 600:
        raise SystemExit(f"monologue is {len(MONOLOGUE)} chars, gate allows 1-600")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MONOLOGUE + "\n")


if __name__ == "__main__":
    main()
