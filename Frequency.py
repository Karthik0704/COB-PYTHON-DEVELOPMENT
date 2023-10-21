import re
from collections import Counter

def process_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text into words
    words = re.findall(r'\w+', text.lower())

    # Count word frequencies
    word_frequencies = Counter(words)

    # Display unique words and their occurrences
    for word, count in word_frequencies.items():
        print(f'{word}: {count} times')

if __name__ == "__main__":
    file_path = r'D:\simple pgm\sample.txt'

    process_text_file(file_path)
