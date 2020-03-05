import sys
    
def histogram(text):
    """
    Creates histogram from text file
    """
    histogram = {}

    for sentences in text:
        sentence = sentences.split()
        for word in sentence:
            histogram[word] = histogram.get(word, 0) + 1

    return histogram

def get_index(word, listogram):
    """Helper function
    """
    current_index = 0

    for item in listogram:
        if item[0] == word:
            return current_index
        current_index += 1 

    return -1
            
def listogram(text):

    listogram = []

    for sentences in text:
        sentence = sentences.split()
        for word in sentence:
            index = get_index(word, listogram)
            if index == -1:
                listogram.append([word, 1])
            else:
                listogram[index][1] += 1

    return listogram

def tuplegram(text):

    tuplegram = []

    pass

def unique_words(histogram):
  
    return len(histogram)
    
def frequency(word, histogram):

    return histogram[word]

if __name__ == '__main__':
    
    with open('plato.txt', 'r') as f:
       
        my_list = f.readlines()
        
    with open('small_file.txt', 'r') as f:
      
        small_file = f.readlines()

    args = sys.argv[1:]
  
    print(listogram(my_list))