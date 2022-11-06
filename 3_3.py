name = (input('Введите имя:'))
age = (input('Введите возраст:'))
city = (input('Введите город:'))
# text = 'Hello %s, age %d, %s' % (name, age, city)
text2 = 'Hello, {}, age {}, city {}'.format(name, age, city)
text3 = f'Hello, {name}, age {age}, city {city}'
print(text2)
print(text3)




