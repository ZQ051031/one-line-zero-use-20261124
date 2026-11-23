"""Write one useless-superpower line to the make.fun output file.

The entry is a single line describing a hilariously useless superpower.
It must be 1-200 characters of UTF-8 text, not only whitespace, and is
written exactly (no trailing newline) to entry.txt in the output dir.
"""

import os
import sys

LINE = "I can talk to animals, but they all think I'm boring."

MAX_CHARS = 200


def validate_entry(text):
    """Check the line satisfies the competition gate."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def output_path():
    """Return the path of the entry file in the output directory."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def write_entry(text, path):
    """Write the validated line to the entry file, exactly as-is."""
    validated = validate_entry(text)
    with open(path, "w", encoding="utf-8") as f:
        f.write(validated)
    return path


def main():
    path = write_entry(LINE, output_path())
    print("wrote %d characters to %s" % (len(LINE), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
