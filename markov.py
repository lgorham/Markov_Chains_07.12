from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    corpus_file = open(file_path, 'r')
    corpus_data = corpus_file.read()

    return corpus_data



def make_chains(text_string):
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
    for i in range(len(split_text)-2):
        # chains[(split_text[i], split_text[i+1])] = chains.get((split_text[i], split_text[i+1]), [])
        # chains[(split_text[i], split_text[i+1])].append(split_text[i+2])
        word_pair = (split_text[i], split_text[i+1])
        following_word = split_text[i+2]
        if word_pair in chains: 
            chains[word_pair].append(following_word)
        else: 
            chains[word_pair] = [following_word]

    # # for first, second in chains.items():
    #     print first, second 

    return chains

# file_path = open_and_read_file('green-eggs.txt')
# print make_chains(file_path)

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    current_key = choice(chains.keys())
    text = current_key[0] + " " + current_key[1]
    for i in range(40):
        next_word = choice(chains[current_key])
        text = text + " " + next_word
        current_key = (current_key[1], next_word)

    # your code goes here

    return text

file_path = open_and_read_file('gettysburg.txt')
as_dict = make_chains(file_path)
print make_text(as_dict)

# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
