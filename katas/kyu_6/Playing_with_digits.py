def dig_pow(n, p):
    x = str(n)
    arr=[]
    for i in range(len(x)):
        arr.append(x[i])
    suma = 0
    for j in range(len(arr)):
        suma = suma + int(arr[j]) ** p
        p = p + 1
    if (suma % n) == 0:
        return suma / n
    else:
        return -1