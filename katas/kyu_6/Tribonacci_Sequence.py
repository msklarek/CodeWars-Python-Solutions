def tribonacci(signature, n):
    arr = []
    if n == 0:
        return []
    p = 0
    if n < 3:
        while p < n:
            arr.append(signature[p])
            p = p + 1
    else:
        arr = signature
        suma = sum(signature)
        p = 3
        while p < n:
            arr.append(suma)
            suma = sum(arr[p - 2:])
            p = p + 1
    return arr