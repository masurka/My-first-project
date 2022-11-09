n = int(input('Введите числовое значение N '))
m = int(input('Введите числовое значение M '))
k = int(input('Введите числовое значение K '))
for i in range(n):
    if n % m == 0 and n > k:
        print(n, end = ' ')
    else:
        print('число не найдено')

