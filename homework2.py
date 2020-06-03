while True:
    number = int(input('enter number:\n'))
    if number > 0:
        while number >= 0:
            print(number, end=' ')
            number -= 1
            continue
        print('')
    elif number < 0:
        while number <= 0:
            print(number, end=' ')
            number += 1
            continue
        print('')

