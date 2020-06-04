list_1 = []
list_2 = []
while True:
    number = input('Enter number ')
    if number != 'stop':
        num = int(number)
        if num < 0:
            list_1.append(num)
            continue
        elif num > 0:
            list_2.append(num)
            continue

    else:
        list_1.reverse()
        list_2.sort()
        list_2.extend(list_1)
        print(list_2)
        break

