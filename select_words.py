"""
Select words from `forman_parsed.csv` with the given length (specified by `--length` argument, default 5)
into an output CSV file (specified by `--output_file` argument, default `forman_parsed_selected_{length}`).
"""
import argparse
import csv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", help="Length of the words to select", default="5")
    parser.add_argument("--output_file", help="Name of the output file.", default="")
    args = parser.parse_args()

    forman_parsed = None
    selected_words = []
    with open("forman_parsed.csv", "r") as f:
        forman_parsed = csv.DictReader(f)
        for row in forman_parsed:
            if int(row["length"]) == int(args.length):
                selected_words.append(row)
    
    filename = f"forman_parsed_selected_{args.length}" if not args.output_file else args.output_file
    with open(f"{filename}.csv", "w+") as f:
        writer = csv.DictWriter(f, fieldnames=["word", "definition", "length"])
        writer.writeheader()
        writer.writerows(selected_words)
    
    print(f"Selected {len(selected_words)} words.")


if __name__ == "__main__":
    main()