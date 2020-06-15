# 1. Создайте список, сохраните в нем имена ваших коллег и друзей.
# Изменился ли идентификатор списка? Отсортируйте список. Ка-
# кой элемент стоит в начале списка? Какой элемент является вто-
# рым?
name = ['Ilya', 'Kate', 'Segrey', 'Andrew']
print(name)
print(id(name))
name.sort()
print(name)
print(name[0])
print(name[1])

# # 2. Создайте кортеж с вашим именем, фамилией и возрастом. Соз-
# дайте список people и присоедините к нему свой кортеж. Создайте
# другие кортежи с соответствующей информацией о ваших друзьях
# и присоедините их к списку. Отсортируйте список. Когда в книге
# будут рассмотрены функции, вы сможете использовать параметр
# key для сортировки списка по любому полю кортежа: имени, фами-
# лии или возрасту.

my_data = ('Roman', 30)
print(type(my_data))
print(my_data)
people = ['first element']
print(type(people))
people.append(my_data[0])
people.append(my_data[1])
print(people)

friend = tuple(['Eugen', '29', 'Sergey', '30', 'Vlad', '30'])
people.append(friend[0])
people.append(friend[1])
people.append(friend[2])
people.append(friend[3])
people.append(friend[4])
people.append(friend[5])
print(people)

# 3. Создайте список с именами ваших друзей. Создайте список с деся-
# тью самыми популярными именами. При помощи операций мно-
# жеств проверьте, входят ли имена кого-либо из ваших друзей в этот
# список.

list_of_friends = ['Sergey', 'Eugen', 'Michael', 'Yuri', 'Vlad']
list_of_people = ['Sergey', 'Maks', 'Mykola', 'Klarisa', 'Larisa', 'Jaffar', 'Murrey', 'Vin', 'Roman']
new_generation = set(list_of_people)
print(type(new_generation))
res_0 = list_of_friends[0] in new_generation
res_1 = list_of_friends[1] in new_generation
res_2 = list_of_friends[2] in new_generation
res_3 = list_of_friends[3] in new_generation
res_4 = list_of_friends[4] in new_generation

print(res_0, res_1, res_2, res_3, res_4)

# 4. Посетите сайт проекта «Гутенберг» 1 и найдите страницу текста из
# Шекспира. Вставьте текст в строку, заключенную в тройные ка-
# вычки. Создайте другую строку с абзацем текста из Ральфа Уолдо
# Эмерсона. Используйте метод .split строк для получения списка
# слов из каждого текста. При помощи операций с множествами най-
# дите общие слова, встречающиеся в текстах обоих авторов, а также
# слова, уникальные для каждого автора.

string_1 = """Запомните — этот 
день обмену и 
возврату не подлежит."""

string_2 = """Лучше находиться в обществе людей лучших, чем вы сами… 
          Выберите знакомых, чье поведение лучше, чем ваше, и вы устремитесь в этом направлении."""

list_1 = set(string_1.split())
print(list_1)
print(type(list_1))

list_2 = set(string_2.split())
print(list_2)

result = list_1 & list_2
print(result)

