def order(sentence):
    a = sentence.split()
    d = {}
    for i in a:
        for k in i:
            if k.isdigit():
                d[i] = k
    b = sorted([(value, key) for (key, value) in d.items()])
    result = ''
    for j in b:
        result = result + ' ' + j[1]
    return result[1:]