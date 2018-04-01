def spin_words(sentence):
    b = sentence.split()
    arr = []
    for i in b:
        arr.append(i)
    result = ''
    for k in arr:
        if len(k) >= 5:
            k = k[::-1]
            result = result + ' ' + k
        else:
            result = result + ' ' + k
    return result[1:]
