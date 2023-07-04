import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def count_and_order_words(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    
    text = soup.get_text()
    
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text.lower())

    words = text.split()

    word_counts = Counter(words)
 
    ordered_words = word_counts.most_common()
    
    return ordered_words

url = 'https://en.wikipedia.org/wiki/Documentation'
ordered_words = count_and_order_words(url)

for word, count in ordered_words:
    print(f'{word}: {count}')