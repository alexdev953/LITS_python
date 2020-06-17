l = [1, 456, 34, 2, 8, 76, 93, 500, 98, 97, 99]


def func1(list_numb, n=5):
    list_numb.sort()
    for values in list_numb[:-n-1:-1]:
        print(values)


func1(l)
