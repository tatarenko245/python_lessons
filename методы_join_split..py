# # Метод join
# Собирает строку из списка

a = list('Roman')
print(a)
del a[0]
print(a)
b = '^'.join(a)
print(b)

# Метод splint
# Собирает список из строк

a = input('Введите ваши слова: ').split()
print(a)

b = input('Введите ваши слова снова:').split('я')
print(b)

# Функция map()
# Нужно из чсиел сделать список чисел
c = list(map(int, input('Введите ваши годы рождения через пробел:').split()))
с = c.sort()
print(c)
print(' '.join(map(str,c)))

#Просстой способ напечатать через пробел:
print(*c)

