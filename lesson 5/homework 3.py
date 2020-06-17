def func3(numb, less_numb):
    a = []
    for i in range(2,numb):
        for j in range(2,i):
            if((i % j) == 0) or i >= less_numb:
                break
        else:
            a.append(i)
    return a

print(func3(50, 10))