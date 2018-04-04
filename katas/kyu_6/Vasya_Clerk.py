def tickets(people):
    #first person has to pay with 25dollars bill
    if people[0] != 25:
        return 'NO'
    price = 25
    d ={}
    #creating dictonary to keep track of numbers of 25, 50 and 100 dollars bills.
    d[25] = 1
    d[50] = 0
    d[100] =0
    for i in range(len(people)-1):
        #case when someone pays with 25 dollars bill and does not need change.
        if people[i+1] == 25:
            d[25] = d[25] + 1
        #case when someone pays with 50 dollars bill and needs 25 change.
        elif people[i+1] == 50:
            if d.get(25) == 0:
                return "NO"
            else:
                d[25] = d[25] -1
                d[50] = d[50] + 1
        #case when someone pays with 100 dollars bills
        #and need 25,50 change or 25,25,25 dollars change.
        elif people[i+1] == 100:
            if d.get(50) != 0 and d.get(25) != 0:
                d[50] = d[50] - 1
                d[25] = d[25] - 1
                d[100] = d[100] + 1
            elif d.get(50) == 0 and d.get(25) >= 3:
                d[25] = d[25] - 3
                d[100] = d[100] + 1
            else:
                return "NO"
    return "YES"