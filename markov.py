from random import choice
import sys 


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    corpus_file = open(file_path, 'r')
    corpus_data = corpus_file.read()

    return corpus_data



def make_chains(text_string, n):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    split_text = text_string.replace('\n',' ').split(' ')
    for i in range(len(split_text)-n):
        # chains[(split_text[i], split_text[i+1])] = chains.get((split_text[i], split_text[i+1]), [])
        # chains[(split_text[i], split_text[i+1])].append(split_text[i+2])
        current_key_iteration = []
        index_pos = i
        while len(current_key_iteration) < n:
            current_key_iteration.append(split_text[index_pos])
            index_pos += 1
        final_key = tuple(current_key_iteration)

        # word_pair = (split_text[i], split_text[i+1])
        following_word = split_text[i+n]
        # print "Final Key: ", final_key, "Next Word: ", following_word
        if final_key in chains: 
            chains[final_key].append(following_word)
        else: 
            chains[final_key] = [following_word]

    # for key, value in chains.items():
    #      print key, value 

    return chains

# file_path = open_and_read_file('green-eggs.txt')
# print make_chains(file_path, 5)

def make_text(chains, n):
    """Takes dictionary of markov chains; returns random text.""" 

    current_key = choice(chains.keys())

    text = ""
    for i in range(0, n):
        text += current_key[i] + " " 

    while current_key in chains.keys():
        next_word = choice(chains[current_key])
        text += " " + next_word
        adjusting_key = list(current_key)
        adjusting_key.append(next_word)
        current_key = tuple(adjusting_key[1:])
        # print adjusting_key
        # print current_key
    # your code goes here

    return text

# file_path = open_and_read_file('green-eggs.txt')
# as_dict = make_chains(file_path)
# print make_text(as_dict)

input_path = sys.argv[1]

n_gram = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n_gram)

# Produce random text
random_text = make_text(chains, n_gram)

print random_text



