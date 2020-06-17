l1 = [1, 10, 13, 15, 23, 22, 10]
l2 = [10, 13, 15, 14, 17, 3]


def func2(list_numb1, lis_numb2):
    l = list_numb1 + lis_numb2
    l3 = []
    for value in l:
        if l.count(value) > 1:
            l3.append(value)
        for values in l3:
            if l3.count(values) > 1:
                l3.remove(values)
    return l3


print(func2(l1, l2))