"""One letter for the day: A.

The entry is a single character and nothing else. Behind it sits the
drink of the morning: coffee -- the fuel keeping a sleep-deprived builder
shipping at dawn. The program checks the letter is one uppercase A-Z
character and writes exactly that character, with no newline, to
/output/entry.txt, so the sealed gate reads a file of exactly 1 char.
"""

from pathlib import Path

DAY_LETTER = None  # derived below from the hidden word, never typed twice
HIDDEN_WORD = "coffee"  # the morning in one word: the fuel keeping a sleep-deprived builder shipping
DRINK_LETTERS = {"coffee": "A", "tea": "B"}  # the brief's code: A for coffee, B for tea


def day_letter() -> str:
    """The entry letter is the brief's code for the hidden word: A for coffee."""
    return DRINK_LETTERS[HIDDEN_WORD]

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def validate(letter: str) -> str:
    """Return the letter once it is exactly one uppercase A-Z character."""
    text = letter.strip()
    if len(text) != 1 or not text.isalpha() or not text.isupper():
        raise ValueError("entry must be exactly one uppercase letter A-Z")
    if text != day_letter():
        raise ValueError("letter does not match the morning's drink")
    return text


def main() -> None:
    letter = validate(day_letter())
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(letter, encoding="utf-8")
    print(letter)
    print(f"Wrote {len(letter)} char to {OUTPUT_FILE} ({HIDDEN_WORD})")


if __name__ == "__main__":
    main()
