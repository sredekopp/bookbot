def get_book_text(path_to_book):
    with open(path_to_book) as book:
        return book.read()

def get_num_words(path_to_book):
    return len(get_book_text(path_to_book).split())

def get_letter_counts(path_to_book):
    letter_dict = {}
    for letter in get_book_text(path_to_book):
        lowered = letter.lower()
        if lowered not in letter_dict:
            letter_dict[lowered] = 1
        else:
            letter_dict[lowered] = letter_dict[lowered] + 1
    
    return letter_dict

def get_num(letter_count):
    return letter_count["num"]

def get_sorted_letter_counts(path_to_book):
    letter_count_list = []
    for letter, count in get_letter_counts(path_to_book).items():
        letter_count = {}
        letter_count["char"] = letter
        letter_count["num"]  = count
        letter_count_list.append(letter_count)
    
    letter_count_list.sort(reverse=True, key=get_num)
    return letter_count_list
    
