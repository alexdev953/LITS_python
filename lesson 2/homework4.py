number = int(input('Enter number:\n'))
a = 1
sum = 0
while a <= number:
    if a % 2 != 0:
        sum += a
        print('Непарне число:',a)
    a +=1
print('Сума непарних чисел = ', sum)
