text = input ("Введите текст: ")
for i in set(text):
    text.count(i)
    print(i, ':', text.count(i))
