import sys
from stats import get_word_count, get_char_count, sort_char_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main(file_path):
    text = get_book_text(file_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    sorted_char_count = sort_char_count(char_count)
    print("============ BOOKBOT ============\n"
    "Analyzing book found at", file_path, "...\n"
    "----------- Word Count ----------\n"
    "Found", word_count, "total words\n"
    "--------- Character Count -------")
    for char_pair in sorted_char_count:
        print(char_pair["char"],": ",char_pair["num"], sep="")
    print("============= END ===============")

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])