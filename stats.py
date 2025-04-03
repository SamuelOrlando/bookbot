def count_words(book):
    return len(book.split())

def count_letters(book):
    letters_dict = {}
    letters_lower = book.lower()
    for letter in letters_lower:
        if letter not in letters_dict:
            letters_dict[letter] = 1
        else:
            letters_dict[letter] += 1
    return letters_dict

def sorted_list(letters):
    sorted_letters = sorted(letters.items(), key=lambda item: item[1], reverse=True)
    return [{"character": key, "count": value} for key, value in sorted_letters]
