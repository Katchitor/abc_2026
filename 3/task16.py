# todo: База данных пользователя.
# Задан массив объектов пользователя

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе

# тип сортировки: 1

#Затем сообщение для ввода
# Ввидите критерии поиска: 16

# Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"

sort_type = input("Введите тип сортировки: ")
criteria = input("Введите критерий поиска: ")

match sort_type:
    case "1":
        users = [user for user in users if user['age']>int(criteria)]
    case "2":
        users = [user for user in users if user['login'].lower().startswith(criteria.lower())]
    case "3":
        users = [user for user in users if user['group']==criteria]

for user in users:
    print(f"Пользователь: {user['login']}, возраст {user['age']} лет, группа {user['group']}")