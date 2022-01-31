"""
Parse `forman_raw.txt` into a csv with three rows: `word`, `definition`, and `length`.
"""
import csv
import re

WORD_PATTERN = re.compile(r"^(?P<word>[A-Za-z’:\-]+)\n\n(?P<definition>[\S\s]+?)\n$", re.MULTILINE)

def main():
    forman_raw = ""
    words = []
    with open("forman_raw.txt", "r") as f:
        forman_raw = f.read()
    matches = WORD_PATTERN.finditer(forman_raw)
    for match in matches:
        word = match.groupdict()["word"].replace("’", "").replace(":", "").replace("-", "")
        words.append({
            "word": word,
            "definition": match.groupdict()["definition"],
            "length": len(word)
        })
    with open("forman_parsed.csv", "w+") as f:
        forman_parsed = csv.DictWriter(f, ["word", "definition", "length"])
        forman_parsed.writeheader()
        forman_parsed.writerows(words)


if __name__ == "__main__":
    main()
