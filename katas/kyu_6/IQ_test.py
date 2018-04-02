def iq_test(numbers):
    a = numbers.split()
    arr = []
    # creating arr of int
    for j in a:
        arr.append(int(j))
    odd = []
    even = []
    #from arr dividing numbers into group two arrays when one is list of odd numbers
    #another one is list of even numbers
    for i in arr:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    #checking which arr (odd or even) had only one element and returning it position in main array arr
    if len(even) == 1:
        return arr.index(even[0]) + 1
    else:
        return arr.index(odd[0]) + 1