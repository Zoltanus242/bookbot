import sys

from stats import get_book_text
from stats import get_num_characters
from stats import print_dictionary_report


def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
        
    try:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_characters = get_num_characters(text)
        character_dictionary = num_characters

        print_dictionary_report(book_path,character_dictionary, text)
        #print(character_dictionary)
    except FileNotFoundError:
        print("File was not found")
        sys.exit(1)

main()