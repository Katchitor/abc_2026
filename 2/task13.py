# В восточном календаре принят 60-летний цикл, состоящий из 12- летних подциклов,
# обозначаемых названиями цвета: зеленый, красный, желтый, белый и черный.
# В каждом подцикле годы носят названия животных: крысы, коровы, тигра, зайца, дракона,
# змеи, лошади, овцы, обезьяны, курицы, собаки и свиньи. По номеру года вывести его название,
# если 1984 год был началом цикла — годом зеленой крысы.

year = int(input("Введите год: "))

year_diff = (year-1984)%12

match year_diff:
    case 0:
        year_name = "Крыса"
    case 1:
        year_name = "Корова"
    case 2:
        year_name = "Тигр"
    case 3:
        year_name = "Заяц"
    case 4:
        year_name = "Дракон"
    case 5:
        year_name = "Змея"
    case 6:
        year_name = "Лошадь"
    case 7:
        year_name = "Овца"
    case 8:
        year_name = "Обезьяна"
    case 9:
        year_name = "Курица"
    case 10:
        year_name = "Собака"
    case 11:
        year_name = "Свинья"

color_diff = (year-1984)%10

match color_diff:
    case 0:
        color_name = "Зеленый"
    case 1:
        color_name = "Зеленый"
    case 2:
        color_name = "Красный"
    case 3:
        color_name = "Красный"
    case 4:
        color_name = "Желтый"
    case 5:
        color_name = "Желтый"
    case 6:
        color_name = "Белый"
    case 7:
        color_name = "Белый"
    case 8:
        color_name = "Черный"
    case 9:
        color_name = "Черный"

print(f"Год {color_name + " " + year_name}")