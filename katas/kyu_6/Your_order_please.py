def order(sentence):
    a = sentence.split()
    d = {}
    for i in a:
        for k in i:
            # building dictonary where key is a word and value
            # is a number of position in a sentence
            if k.isdigit():
                d[i] = k
    # sorting dictory by values
    b = sorted([(value, key) for (key, value) in d.items()])
    result = ''
    # building a sentece made by keys and position depends of a value
    for j in b:
        result = result + ' ' + j[1]
    return result[1:]

