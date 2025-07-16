from stats import get_num_words, get_char_count, get_sorted_char_count
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    else:
        book_path = sys.argv[1]
    
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        sorted_char_count = get_sorted_char_count(text)

        print("============ BOOKBOT ============")
        print(f"Analysing book found at {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("---------- Character Count -------")

        for char, count in sorted_char_count:
            if char.isalpha():
             print(f"{char}: {count}")

        print("============= END ===============") 


def get_book_text(path):
    with open(path) as f:
        return f.read()




main()
