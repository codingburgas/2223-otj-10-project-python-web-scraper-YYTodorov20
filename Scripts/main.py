import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def count_and_order_words(url, sort_by_frequency=True):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text.lower())
    words = text.split()
    word_counts = Counter(words)

    if sort_by_frequency:
        ordered_words = word_counts.most_common()
    else:
        ordered_words = sorted(word_counts.items(), key=lambda x: x[0])

    return ordered_words

def print_ordered_words(ordered_words):
    for word, count in ordered_words:
        print(f'{word}: {count}')

def main():
    url = 'https://en.wikipedia.org/wiki/Documentation'
    
    while True:
        print("Choose an option:")
        print("1. Order by frequency")
        print("2. Order alphabetically")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            ordered_words = count_and_order_words(url, sort_by_frequency=True)
            print_ordered_words(ordered_words)
        elif choice == '2':
            ordered_words = count_and_order_words(url, sort_by_frequency=False)
            print_ordered_words(ordered_words)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == '__main__':
    main()
