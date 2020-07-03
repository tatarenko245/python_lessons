# Используем прерывание
numbers = [3, 5, 9, -1, 3, 1]
result = 0
for item in numbers:
    if item < 0:
        break
    result += item
    # result=result+item
print(result)

# Используем команду continue
numbers = [7, 8, 9, 1, -1, 3, 1, 1]
result = 0
for item in numbers:
    if item < 0:
        continue
    result += item
print(result)

# Проверяем принадлежноть с помощью оператора in
animals = ['cat', 'dog', 'bird']
result = 'cat' in animals
print(result)
# узнаем индекс кота
cat_index = animals.index('cat')
print(cat_index)
# узнаем индекс собаки
dog_index = animals.index('dog')
print(dog_index)
# Узнаем индекс птички
bird_index = animals.index('bird')
print(bird_index)

# Удалим атрибут при итерации. Удалим имя Paul
names = ['John', 'Paul', 'Ringo', 'George']
for name in names:
    if name == 'Paul':
        names.remove(name)
print(names)

# Удалим атрибут при итерации. Оставим имя Paul
names = [input('Enter the names of Beatles:')]
for name in names:
    if name =='Paul':
        print('Paul McCartney is bassist')
    if name == 'Ringo':
       print('Ringo Starr is drummer')
    # print(names)