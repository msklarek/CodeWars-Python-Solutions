def find_outlier(integers):
    arr = len(integers) - 2
    for i in range(arr):
        if integers[i] % 2 == 0 and integers[i + 1] % 2 == 0:
            for k in integers:
                if k % 2 != 0:
                    return k
        elif integers[i + 2] % 2 != 0:
            for k in integers:
                if k % 2 == 0:
                    return k
    return 1

