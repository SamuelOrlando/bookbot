from stats import count_words, count_letters, sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        raise SystemExit(1)

    book = get_book_text(file_path)
    word_count = count_words(book)
    letter_count = count_letters(book)
    sorted_dict = sorted_list(letter_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count ---------")
    for item in sorted_dict:
        if item["character"].isalpha():
            print(f"{item['character']}: {item['count']}")
    print("============= END =============")

main()
