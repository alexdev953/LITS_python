text = input('Enter text: ')
text2 = []
for strings in list(text):
    if strings.islower():
        text2.append(strings.upper())
    elif strings.isupper():
        text2.append(strings.lower())
print(''.join(text2))
