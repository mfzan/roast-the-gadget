"""One-Line Roast: The Gadget You Use Every Day.

Writes a single roast line to /output/entry.txt. The line targets one
gadget (my phone) and one flaw only a daily user would notice: the alarm
that never lets me oversleep is itself dead by four in the afternoon.
"""

import os

# The roast: one line, 122 characters, well inside the 200 limit.
ROAST = (
    "My phone drags me out of bed at 6am sharp every day \u2014 "
    "then dies by 4pm, the only alarm clock that can't stay awake itself."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    line = ROAST.strip()
    if not line or len(line) > MAX_CHARS or "\n" in line:
        raise ValueError("roast must be one line of 1-200 characters")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")

    # Only the output FILE is made world-readable; the grader collects
    # outputs as another user (65534). Never chmod the /output directory.
    os.chmod(OUTPUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
