# amanu
> (N.) word, language, speech.

CSV of Kapampangan words extracted from Forman's Kapampangan Words[^1] PDF.

`forman_parsed.csv` has three columns: `word`, `definition`, and `length` (counting the word length).
`forman_parsed_selected_5.csv` has the same columns as above, but only includes words of length `5`.

## Usage

1. Run `python parse_forman.py` to re-create `forman_parsed.csv` from the raw `forman_raw.txt` file, which is an abridged txt conversion of the original book PDF.
2. Run `python select_words.py [--length=5] [--output_file=new_file]` to select words of desired length into a new CSV file.

[^1]: [Forman, M. L. (2019). Kapampangan Words (2019 Edition). University of Hawaii Press.](https://books.google.com/books/about/Kapampangan_Dictionary.html?id=v8AWyAEACAAJ&redir_esc=y)
