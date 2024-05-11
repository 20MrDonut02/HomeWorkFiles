with open('text.txt', 'r', encoding='utf-8') as f:
    file_as_str = f.read()  # Читаем информацию из файла

file_as_list = file_as_str.split('\n')  # разделяем информацию по строчно

# уберем числа количества ингридиентов для дальнейшей работы с данными

for i in file_as_list:
    if i.isdigit():
        file_as_list.remove(i)

# разделим данные ингридиентов для каждого блюда

recipes = []
res = []
for item in file_as_list:

    if item != '':
        res.append(item)
    else:
        recipes.append(res)
        res = []

# получаем при вводе print(recipes) следующее:

# [['Омлет', 'Яйцо | 2 | шт', 'Молоко | 100 | мл', 'Помидор | 2 | шт'],
# ['Утка по-пекински', 'Утка | 1 | шт', 'Вода | 2 | л', 'Мед | 3 | ст.л', 'Соевый соус | 60 | мл'],
# ['Запеченный картофель', 'Картофель | 1 | кг', 'Чеснок | 3 | зубч', 'Сыр гауда | 100 | г']]


# создадим словарь cook_book,куда будем заносить наши блюда

cook_book = {}

for names in recipes:
    name = names[0]
    cook_book[name] = []
    for ing in names[1:]:
        ing_str = ing.split(" | ")
        cook_book[name].append({'ingredient_name': ing_str[0],
                                'quantity': int(ing_str[1]),
                                'measure': ing_str[2]})

print(cook_book)


# {'Омлет': [{'ingredient_name': 'Яйцо', 'quantity': '2', 'measure': 'шт'},
#            {'ingredient_name': 'Молоко', 'quantity': '100', 'measure': 'мл'},
#            {'ingredient_name': 'Помидор', 'quantity': '2', 'measure': 'шт'}],
#  'Утка по-пекински': [{'ingredient_name': 'Утка', 'quantity': '1', 'measure': 'шт'},
#                       {'ingredient_name': 'Вода', 'quantity': '2', 'measure': 'л'},
#                       {'ingredient_name': 'Мед', 'quantity': '3', 'measure': 'ст.л'},
#                       {'ingredient_name': 'Соевый соус', 'quantity': '60', 'measure': 'мл'}],
#  'Запеченный картофель': [{'ingredient_name': 'Картофель', 'quantity': '1', 'measure': 'кг'},
#                           {'ingredient_name': 'Чеснок', 'quantity': '3', 'measure': 'зубч'},
#                           {'ingredient_name': 'Сыр гауда', 'quantity': '100', 'measure': 'г'}]}


def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for dish in dishes:
        for names in cook_book[dish]:
            ing = names['ingredient_name']
            if ing not in res.keys():
                res[ing] = {'measure': names['measure'],
                            'quantity': names['quantity'] * person_count}

    return res


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


# Напишем функцию для открытия файла

def read_file(name_file):
    line_count = 0
    list_file = []
    dict_file = {}
    with open(name_file, encoding='utf-8') as f:
        for line_file in f:
            line_count += 1
            list_file.append(line_file)
        value = [name_file] + [line_count] + list_file
        dict_file[line_count] = value
    return dict_file


dict1 = read_file('1.txt')
dict2 = read_file('2.txt')
dict3 = read_file('3.txt')

sum_dict = dict1 | dict2 | dict3
sort_dict = dict(sorted(sum_dict.items()))

with open('result.txt', 'w', encoding='utf-8') as f:
    for key in sort_dict.keys():
        for read in sort_dict[key]:
            f.write((str(read).strip() + '\n'))
