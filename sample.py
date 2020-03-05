import sys
import random
from histogram import histogram
import re

def random_word(text): 

    random_index = random.randint(0, sum(text.values()))

    total = 0

    for word,count in text.items():
        total += count
        
        if total >= random_index:
            
            return word


def read_file(source_text):

    with open(source_text, 'r') as f:

        words = f.read()

        words_list = re.sub(r'[^a-zA-Z\s]', '', words).lower()

        word_list = words_list.split()
        
    return word_list

if __name__ == "__main__":
    lines = read_file("plato.txt")
    text = histogram(lines)
    args = sys.argv[:1]
    print(random_word(text))

