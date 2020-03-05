from dictogram import Dictogram
from sample import random_word
from random import choice

class MarkovChain:

    def __init__(self, word_list):
        #The Markov chain will be a dictionary of dictionaries
        #Example: for "one fish two fish red fish blue fish"
        #{"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
        self.markov_chain = self.build_markov(word_list)
        self.first_word = list(self.markov_chain.keys())[0]

    def build_markov(self, word_list):

        markov_chain = {}

        for i in range(len(word_list) - 1):
            #get the current word and the word after
            current_word = word_list[i]
            next_word = word_list[i+1]

            if current_word in markov_chain.keys(): #already there
                #get the histogram for that word in the chain
                histogram = markov_chain[current_word]
                #add to count
                histogram.dictionary_histogram[next_word] = histogram.dictionary_histogram.get(next_word, 0) + 1
                histogram.tokens += 1
                
            else: #first entry
                markov_chain[current_word] = Dictogram([next_word])

        return markov_chain

    def walk(self, num_words):
        #TODO: generate a sentence num_words long using the markov chain
        sampled_list = []

        sampled_list.append(choice(list(self.markov_chain.keys())))

        for i in range(num_words):

            current_word = sampled_list[i]

            random_word = self.markov_chain[current_word]

            random_word = random_word.sample()

            sampled_list.append(random_word)
        
            
        finished_sentence = ' '.join(sampled_list)

        return finished_sentence
            
    def print_chain(self):

        for word, histogram in self.markov_chain.items():

            print(word, histogram.dictionary_histogram)

markov_chain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])