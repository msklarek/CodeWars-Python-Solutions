def digital_root(n):
    a = str(n)
    suma = 0
    while len(a) > 1:
        arr = []
        for i in range(len(a)):
            arr.append(a[i])
        suma = 0
        for j in range(len(arr)):
            suma = suma + int(arr[j])
            a = str(suma)
    return suma
