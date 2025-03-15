def get_book_text(file_path):
    with open(file_path) as f:
        teksti = f.read()
        return teksti
    
def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_num_characters(book_text):

    book_text = book_text.lower()
    characters = {}
    for character in book_text:
        try:
            characters[character] += 1
        except KeyError:
            characters[character] = 1

    return characters

def sort_on(dict):
    return dict["num"]

def sort_character_dictionary(dictionary):
    char_dict = []
    for key in dictionary:
        new_dict = {"char" : key, "num" : dictionary[key]}
        char_dict.append(new_dict)
    char_dict.sort(reverse=True, key=sort_on)
    return char_dict


#DOTO
def print_dictionary_report(book_path, char_dictionary, book_text):
    char_dictionary = sort_character_dictionary(char_dictionary)
    print("============ BOOKBOT ============\n"
          f"Analyzing book found at {book_path}\n"
          "----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    for dict in char_dictionary:
        if not dict["char"].isalpha():
            continue
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")