# 1 Завдання:
# Програма, яка вибирає зі введеної строки цифри і виводить їх через кому
# Наприклад:
# st = 'as 23 fdfdg544' - введена строка
# 2,3,5,4,4 - виведено в консолі

#1: З list comprehension
# st = 'as 23 fdfdg544'
# digits = [char for char in st if char.isdigit()]
# print(",".join(digits))
#Або
st = 'as 23 fdfdg544'

digits = []
for char in st:
    if char.isdigit():
        digits.append(char)

print(digits)

# 2 Завдання:
# написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#  st = 'as 23 fdfdg544 34' #введена строка
#  23, 544, 34              #вивело в консолі

st = 'as 23 fdfdg544 34'

digits = []
temp = ''

for char in st:
    if char.isdigit():
        temp += char
    else:
        if temp:
            digits.append(temp)
            temp = ''

if temp:
    digits.append(temp)

print(", ".join(digits))

# 3 Завдання:

# list comprehension

# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'
uppercase_list = [char.upper() for char in greeting]
print(uppercase_list)

# 4 Завдання:
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
squared_odds = [x**2 for x in range(51) if x % 2 != 0]
print(squared_odds)

#5 Завдання:

# function
# - створити функцію яка виводить ліст
# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# - створити функцію яка повертає найбільше число з ліста
# - створити функцію яка повертає найменьше число з ліста
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# function
# - створити функцію яка виводить ліст:
my_list = [1, 2, 3, 'a', 'b', 'c']

def show_list():
    print(my_list)

show_list()

# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def show_numbers(a,b,c ):
    largest =max(a,b,c)
    return largest

result =  show_numbers(10,20,30)
print(f"result:{result}")

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def random_numbers(*args):
    if args:
        largest = max(args)
        smallest = min(args)
        print(f"Найбільше число: {largest}")
        return smallest
    else:
        return None

result2 = random_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"Найменше число: {result2}")

# - створити функцію яка повертає найбільше число з ліста
def max_num_from_list(list1):
    result_list = max(list1)
    return result_list

result3 = max_num_from_list([100, 200, 300])
print(f'Найбільше число з ліста: {result3}')

# - створити функцію яка повертає найменше число з ліста
def min_num_from_list2(list1):
    result_list = min(list1)
    return result_list

result4 = min_num_from_list2([100, 200, 300])
print(f'Найменше число з ліста: {result4}')

#- створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def sum_numbers(some_list):
    if some_list:
        result5 = sum(some_list)
        return result5
    else:
        return None
result6 = sum_numbers([10,10,10,10,10])
print(f"Сума чисел: {result6}")

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def arithmetic(some_list):
    if some_list:
        result7 = sum(some_list) / len(some_list)
        return result7
    else:
        return None
result8 = arithmetic([10,10,10,10,10])
print(f"Середнє арифметичне чисел: {result8}")

################################################################################################
#2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
# 1)Дан list:
  #list_task = [22, 3,5,2,8,2,-23, 8,23,5]
  #- знайти мін число
  #- видалити усі дублікати
  #- замінити кожне 4-те значення на 'X'

list_task = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

def min_list_task_number(lst):
    result12 = min(lst)
    return result12

print(min_list_task_number(list_task))


def remove_duplicates(list_task3):
    # Використовуємо set для видалення дублікатів
    no_duplicates = list(set(list_task3))
    return no_duplicates

result10 = remove_duplicates(list_task)
print(f"Список без дублікатів: {result10}")


#list_task = [22, 3,5,2,8,2,-23, 8,23,5]
# - замінити кожне 4-те значення на 'X'
list_task2 = [22, 3,5,2,8,2,-23, 8,23,5]
for i in range(3,len(list_task2),4):
    list_task2[i] = 'X'
print(list_task2)

#2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def print_empty_square(side_length):
    # Перевіряємо, чи сторона квадрата більша або дорівнює 1
    if side_length < 1:
        print("Сторона квадрата повинна бути більше або дорівнює 1.")
        return

    border_row = '*' * side_length

    print(border_row)

    for _ in range(side_length - 2):
        print('*' + ' ' * (side_length - 2) + '*')

    if side_length > 1:
        print(border_row)

side_length = 5
print_empty_square(side_length)

#3) вывести табличку множення за допомогою цикла while
def print_multiplication_table(size):
    row = 1
    while row <= size:
        column = 1
        while column <= size:
            print(f"{row * column:4}", end=' ')
            column += 1
        print()
        row += 1

size = 10
print_multiplication_table(size)


