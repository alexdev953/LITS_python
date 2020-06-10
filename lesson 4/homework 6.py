text = input('enter text: ')
if text[0].isnumeric() and text.find('.') != -1:
    print('float')
elif text.isdigit():
    print('numeric')
else:
    print(text)
