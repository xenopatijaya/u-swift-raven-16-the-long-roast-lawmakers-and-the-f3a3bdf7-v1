"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (161 characters, one sentence) to
/output/entry.txt, per the competition gate: UTF-8 text of 1-320
characters, not only whitespace.

The line: lawmakers want a law for every byte on the internet, yet
the lawmaker writing the bill just discovered it is a .docx, and his
solution is to rename it .pdf and hope. Setup (authority) -> turn
(incompetence) -> punch on the last words ("and hope").

Local runs may redirect the output directory with the
MAKEFUN_OUTPUT_DIR environment variable; the graded run uses the
kit's /output location.
"""

import os

ENTRY = (
    "They want a law for every byte on the internet, yet the lawmaker "
    "writing it just discovered his bill is a .docx, and his solution "
    "was to rename it .pdf and hope."
)


def main() -> None:
    # Gate self-check: one sentence, 1-320 chars, not only whitespace.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 320, f"entry is {len(text)} chars"
    assert text.endswith("."), "entry must end with a full stop"
    assert ". " not in text, "entry must be a single sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(text)


if __name__ == "__main__":
    main()
