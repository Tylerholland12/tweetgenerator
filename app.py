from flask import Flask, render_template
from create_sentence import create_sentence
import os
from sample import read_file
from markov import MarkovChain

app = Flask(__name__)

@app.route('/')
def render_page():
        
    my_list = read_file('plato.txt')

    chain = MarkovChain(my_list)

    num_words = int(10) - 1
    
    my_sentence = chain.walk(num_words)  

    my_sentence_2 = chain.walk(num_words)

    my_sentence_3 = chain.walk(num_words)

    my_sentence_4 = chain.walk(num_words)

    my_sentence_5 = chain.walk(num_words)
    
    return render_template('index.html', sentence=my_sentence,
                                        sentence2=my_sentence_2,
                                        sentence3=my_sentence_3,
                                        sentence4=my_sentence_4,
                                        sentence5=my_sentence_5)

if __name__ == '__main__':
    app.run(debug=True)