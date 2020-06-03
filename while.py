s = input("Enter yes/no: ")
while s != "yes" and s != "no":
    s = input("Enter yes/ no: ")
print("thank you, you have entered: " + s )

# наибольшее целое число, чей квадрат не превышает х
x = int(input("Enter integer: "))
result = 0
while (result + 1) * (result + 1) <= x:
    result = result +1
print(result)