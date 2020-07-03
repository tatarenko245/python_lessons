# Цикл while віполняется пока условие истинно
#  Конструкция цикла while
# while условие:
#         операторы

# # Example 1
# response = ""
# while response != "exit":
#     response = input('Type exit to exit, please: ')
#
# # Example 2
# n = 1
# while n <= 3:
#     print('n =', n)
#     n += 1
#
# # Example 3
# number = 0
# while number >= 0:
#     number = int(input('Введите положительное, целое число: '))
# print('Вы должны ввести целое, положительное число число')

# Example 4
# n = 2
# while True:
#     print(n)
#     n **= 2

# Операторы break и continue
# break - завершает весь цикл досрочно
# continue - завершит текущую итерацию цикла

# Example 5
# while True:
#     print("enter 'exit' to exit loop")
#     response = input('enter something: ')
#     if response == 'exit':
#         break
# print('loop has stopped')


# Example 6
# name = None
# while True:
#     print('Menu:')
#     print('1. Enter name')
#     print('2. Print greeling')
#     print('3.Quit')
#
#     response = input('Please, choose an action: ')
#     print()
#
#     if response == "1":
#         name = input('Enter your name: ')
#         if name:
#             print("Hello, ", name, "!")
#             print()
#     elif response == "2":
#         if name:
#             print("Hello, ", name, "!", sep="")
#         else:
#             print("I don't know your name. Choose the 1. Enter your name")
#     elif response == "3":
#         break
#     else:
#         print("Incorrect input")

# Example 7 оператор continue
# number = 0
# while number < 10:
#     number += 1
#     if number == 5:
#         continue
#     print("Current number is ", number)

# Example 8 ветка else исполняется когда условие стало ложным
# counter = 5
# while counter:
#     print(counter)
#     counter -= 1
#
# else:
#     print("Loop is complete")
#     print('counter =', counter)

# Example 9 с приминением оператора break - прекращает выполнение цикла
# Пусть количество попыток ввода пароля ==3
# attempts_left = 3
# while attempts_left > 0:
#     attempts_left -= 1
#     password = input("Enter your password: "
#                      "(you have {} attempts left): ".format(attempts_left+1))
#     if password == "123qw":
#         print("Password is correct")
#         break
#     else:
#         print("Invalid password")

# Example 10 цикл со счетчиком for
# for i in range(10):
#     print("i =", i)

# певоре значение включая, а последнее не включая от 3 до 9
# for i in range(3, 10):
#     print(i)

# Добавим еще и шаг
# for i in range(2, 15, 2):
#     print("i с шагом 2 = ", i)

# Отрицательный шаг от большего к меньшему
# for i in range(10, 0, -1):
#     print("i с шагом -1 от большего к меньшему = ", i)

# Example 11 Задача с обратным отсчетом до старта
# i = 10
# while i:
#     print(i)
#     i -= 1
#     if i == 0:
#         print("start")

# Example 12 Вложенные циклы
# for row in range(5):
#     for column in range(30):
#         print('*', end="")
#     print()
