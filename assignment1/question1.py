
def common_words(filename):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """
    
    import re, itertools
    
    # open file for reading and copy its contents
    file = open(filename, "r")
    contents = map(lambda x: x.split(" "), file.readlines())
    file.close()
    
    # combine the lines of the text that were read in
    combined = list(itertools.chain(*contents))

    # count and store the words from the text
    words = {}
    for word in combined:
        word = re.sub(r'\W+', '', word).lower()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    # sort the list of words in order of their usage
    words = sorted(words, key=words.get, reverse = True)

    return words

def common_words_min(filename, min_chars):
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """
    
    import re, itertools
    
    # open file for reading and copy its contents
    file = open(filename, "r")
    contents = map(lambda x: x.split(" "), file.readlines())
    file.close()
    
    # combine the lines of the text that were read in
    combined = list(itertools.chain(*contents))
    
    # count and store the words from the text
    words = {}
    for word in combined:
        word = re.sub(r'\W+', '', word).lower()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    
    # sort the list of words in order of their usage
    words = sorted(words, key=words.get, reverse = True)

    # remove any words that are not a min num of chars
    words = filter(lambda x: len(x) >= min_chars, words)

    return words


def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    
    import re, itertools
    
    # open file for reading and copy its contents
    file = open(filename, "r")
    contents = map(lambda x: x.split(" "), file.readlines())
    file.close()
    
    # combine the lines of the text that were read in
    combined = list(itertools.chain(*contents))
    
    # count and store the words from the text
    words = {}
    for word in combined:
        word = re.sub(r'\W+', '', word).lower()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    
    # sort the list of words in order of their usage
    words_sorted = sorted(words, key=words.get, reverse = True)

    # remove words under min_chars and create new list of tuples
    tuples = []
    for word in words_sorted:
        if len(word) >= min_chars:
            tuples.append((word, words[word]))

    return tuples

def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """

    try:
        common_words_tuple(filename, min_chars)
    except IOError, e:
        print e[1]

