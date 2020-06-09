# Задача 1
import string

age = int(input("Enter your age, please: "))
old = None
if age >= 18:
    old is True
    print("You have an access")
else:
    old is False
    print("You don't have an access")

# Задача 2
name = input("Введите Ваше имя, пожалуйста: ")
second_half = name[0].upper() in string.ascii_uppercase[len(string.ascii_uppercase)//2:]
if second_half is True:
    print("Ваше имя начинается на букву со второй половины алфавита")
else:
    print("Ваше имя начинается на букву с первой половины алфавита")

# Задача 3
names = ["Bogdan", "Mykola", "Ilya"]
bool(names)
type(names)
if names is True:
    print("The class is not empty")
else:
    print("The class is empty")

# Задача 4
car = "Toyota"
if car is None:
    print("You have a car")
else:
    print("Sorry, we are looking car for you")

