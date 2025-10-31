import sys
from stats import get_num_words
from stats import get_sorted_letter_counts

def main(args):
    if not len(args) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = args[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(path_to_book)} total words")
    print("--------- Character Count -------")
    for letter in get_sorted_letter_counts(path_to_book):
        if not letter["char"].isalpha():
            continue
        print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")

main(sys.argv)
