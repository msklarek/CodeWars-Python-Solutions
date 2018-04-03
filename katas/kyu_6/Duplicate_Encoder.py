def duplicate_encode(word):
    result = ''
    b= word.lower()
    for i in b:
        if b.count(i) == 1:
            result = result + '('
        else:
            result = result + ')'
    return result