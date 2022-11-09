a = int(input('Ввдите первое число: '))
x = input('Введите знак: ')
b = int(input('Введите второе число: '))
if x == '+':
    print(a+b)
elif x == '-':
    print(a-b)
elif x == '*':
    print(a*b)
elif x == '**':
    print(a**b)
elif x == "/":
    if b == 0:
        print('На ноль делить нельзя')
else:
        print(a/b)
