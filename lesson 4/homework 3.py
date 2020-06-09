text = input('Enter text: ').replace('—', '').replace(' ', '').replace(',', '').replace('!', '').replace('?', '').lower()
revers = text[::-1]
if text == revers:
    print('Поліндром')
else:
    print('Не поліндром')
