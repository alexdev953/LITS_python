l1 = [1, 2, 3, 4, 10, 13, 15, 14, 17, 3, 23, 22, 15, 36, 44, 55, 36, 37, 2, 1, 53]
l1.sort()
print('Before magic: ', l1)
for values in l1:
    if l1.count(values) > 1:
        l1.remove(values)
print('After magic: ', l1)

