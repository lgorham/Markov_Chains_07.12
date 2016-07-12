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

    start = 0
    stop = 1 
    following = 2


    split_text = text_string.replace('\n',' ').split(' ')
    for i in range(len(split_text)):
        if following < (len(split_text)-1):
            if (split_text[start], split_text[stop]) in chains: 
                chains[(split_text[start], split_text[stop])].append(split_text[following])
            else: 
                chains[(split_text[start], split_text[stop])] = [split_text[following]]
            start += 1 
            stop += 1
            following += 1

    # for first, second in chains.items():
    #     print first, second 
        
    return chains

file_path = open_and_read_file('green-eggs.txt')
print make_chains(file_path)

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
