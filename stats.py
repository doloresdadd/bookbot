from collections import Counter

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    lowercase_text = text.lower()
    char_count = Counter(lowercase_text)
    return char_count

def get_sorted_char_count(text):
    lowercase_text = text.lower()
    char_count = Counter(lowercase_text)
    char_count_sorted = sorted(char_count.items(), key=lambda item: item[1], reverse=True)  
    return char_count_sorted
