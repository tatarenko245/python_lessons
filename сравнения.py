# Специальный метод сравнения
name = input("Enter your name, please: ")
dreamteam = None
if name == "Petro" or \
        name == "Ringo" or \
        name == "Mykola":
    dreamteam = True
else:
    dreamteam = False
print(dreamteam)

# Поверка принадлежности
beatles = {"George", "Ringo", "John", "Paul"}
beatle = name in beatles
if name == "Gero" and not beatle in beatles:
    last_name = "Revere"
    print(name + last_name)
else:
    print("I do not know what you mean")
