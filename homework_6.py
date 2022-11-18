import random
# task_1
some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(some_list)):
    if_sign = 0
    count = 0
    for search_digit in some_list[i]:
        if search_digit.isdigit():
            count+=1
        else:
            if_sign+=1
    if if_sign != 0 and count != 0:
        some_list[i] = f'"{some_list[i][0]}0{some_list[i][1:]}"'
    if count < 2 and count != 0 and if_sign == 0:
        some_list[i] = '"0'+some_list[i]+'"'
        count = 0
    elif count > 1 and if_sign == 0:
        some_list[i] = '"'+some_list[i]+'"'
        count = 0

print(" ".join(some_list))

#task_2

some_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for item in some_list:
    some_str = item.split(' ')
    print(f'Привет {some_str[-1].capitalize()}')

#task_3
# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
def sort_max(s_list):
    for i in range(len(s_list)-1):
        for j in range(len(s_list)-i-1):
            if s_list[j] > s_list[j+1]:
                s_list[j], s_list[j+1] = s_list[j+1], s_list[j]
    return s_list

def sort_min(s_list):
    for i in range(len(s_list)-1):
        for j in range(len(s_list)-i-1):
            if s_list[j] < s_list[j+1]:
                s_list[j], s_list[j+1] = s_list[j+1], s_list[j]
    return s_list

def add_rk(s_list):
    for i in  range(len(s_list)):
        s_list[i] = str(s_list[i]).split('.')

        s_list[i][0] = f'{s_list[i][0]} руб. '
        if len(s_list[i][1])==1:
            s_list[i][1] = f'{s_list[i][1]}0 коп.'
        else:
            s_list[i][1] = f'{s_list[i][1]} коп.'
        s_list[i] = s_list[i][0]+s_list[i][1]
    return s_list

def return_top(s_list, numb):
    return s_list[: numb]


price_list = [round(random.uniform(0,9),2) for i in range(20)]
max_l = sort_max(price_list)
print(max_l)
rub_max_l = add_rk(max_l)
print(rub_max_l)
print(return_top(rub_max_l, 5))
min_l = sort_min(price_list)
print(min_l)
rub_min_l = min_l
print(return_top(rub_min_l, 5))


