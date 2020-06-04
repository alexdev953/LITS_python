l1 = [1, 2, 3, 4, 10, 13, 15, 14, 17, 23, 22, 36, 44, 55, 37]
print('Before magic: ', l1)
for values in l1:
    ind = l1.index(values)
    if values % 2 == 0:
        l1[ind] = 0
    elif values % 2 != 0:
        l1[ind] = l1[ind] ** 2
print('After magic: ', l1)

