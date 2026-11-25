import os

SENTENCE = (
    "My mother's pork-and-chive dumplings — forty at our kitchen table the night "
    "before I left for university, vinegar sharp on my tongue, steam stinging my "
    "eyes, and her pretending it stung hers too."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
