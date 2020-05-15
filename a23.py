'''Write a function filter_long_words() that takes a list of words and an integer n and returns the list
of words that are longer than n.'''
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(find_longest_word(["satvik", "john", "sam"]))