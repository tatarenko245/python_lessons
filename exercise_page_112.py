# Задача на определение является ли год высокосным или нет
year = int(input("enter your year: "))
if (year % 4 == 0) and (year % 100 != 0) or (year % 100 == 0) and (year % 400 == 0):
    print("year is leap year")
else:
    print("year does not leap year")

# Задача на определение явдяется ли число четным или нет
number = int(input("Enter your number, please: "))
if number %2 == 0:
    print('Your number is even number')
else:
    print('Your number does not even number')
