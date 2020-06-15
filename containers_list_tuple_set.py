# Списки. Это изменяемые последовательности.

# Создадим пустой список первым способом
name_1 = list()
print(name_1)

# Создадим пустой список вторым способом
name_2 = []
print(name_2)

name = ['Fred', 'John']
list('Matt')
name.append('Roman')
print(name)

# Выполним вставку в список
name.insert(1, 'Ilya')
print(name)

# Выполним удаление элемента
name.remove('Ilya')
print(name)

# Выполним удаление элемента из списка по его индексу
del name[1]
print(name)

# Добавим элементы в список, а потом отсортируем его
cars = ['toyota', 'kia', 'nissan', 'suzuki']
print(cars)
cars.sort()
print(cars)

# Сортировка с помощью ключа
things = [2, 'abc', 'Zebra', '1']
things.sort(key=str)
print(things)

# Использование функции range
nums = range(5)
list(nums)
print(nums)

nums_1 = range(2, 8)
print(nums_1)

# В функции range() есть необязательный атрибут - приращивание
nums_2 = range(3, 9, 2)
print(nums_2)

# Кортежи. Это неизменяемые последовательности.

# Создадим пустой кортеж
# Первый способ
a = tuple()
print(a)

# Второй способ
b = ()
print(b)

# Создадим кортеж с одним элементом
# Первый способ
one_1 = tuple([1])
print(one_1)

# Второй способ
one_2 = (1,)
print(one_2)

# Третий способ
one_3 = 1,
print(one_3)

# Создадим кортеж с несколькими элементами
p = ('Stepan', 'Mylola',)
print(type(p))

# Множества.Set
# Используется для удаления дубликатов
digits = [0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(digits)
digit_set = set(digits)
print(digit_set)

# Множество можно передать в фигурніх скобках {}
digit_set_2 = {0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9}
print(digit_set_2)

# Чтобы проверить принадлежность, используется операция in
digit_set_3 = {0, 1, 2, 3, 4, 4, 5, 5, 6, 7, 8}
result = 9 in digit_set_3
print(result)
result = 4 in digit_set_3
print(result)

# Операции с множествами
# 1) Операция вычитания
odd_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
odd_2 = {1, 3, 5, 7, 9}
result = odd_1 - odd_2
print(result)

# 2) Операция пересечения
odd_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
odd_2 = {2, 3, 4, 5, 6}
result = odd_1 & odd_2
print(result)

# 3) Операция объединения
odd_1 = {0, 1, 2, 3, 4}
odd_2 = {5, 6, 7, 8, 9}
result = odd_1 | odd_2
print(result)

# 4) Операция исключающего ИЛИ
odd_1 = {0, 1, 2, 3, 4}
odd_2 = {0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9}
result = odd_1 ^ odd_2
print(result)

