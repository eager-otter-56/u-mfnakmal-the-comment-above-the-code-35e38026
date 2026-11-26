import os
import stat

ENTRY_TEXT = "// WARNING: removing this function breaks 613 tests, 2 dashboards, and my own alibi for approving it."


def main():
    # Gate: entry must be UTF-8 text of 1 to 200 characters, not only
    # whitespace, and a single line.
    assert 1 <= len(ENTRY_TEXT) <= 200, "entry length out of gate"
    assert ENTRY_TEXT.strip(), "entry is only whitespace"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
