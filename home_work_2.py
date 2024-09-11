#1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
#2) протипізувати перше завдання

from typing import List, Callable, Tuple

def notebook() -> Tuple[Callable[[str], None], Callable[[], List[str]]]:
    todo_list: List[str] = []

    def add_todo(todo: str) -> None:
        todo_list.append(todo)

    def get_all() -> List[str]:
        return todo_list

    return add_todo, get_all

# Використання
add_todo, get_all = notebook()

add_todo("Купити продукти")
add_todo("Написати код")
add_todo("Прочитати книгу")

print(get_all())  # ['Купити продукти', 'Написати код', 'Прочитати книгу']

#3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#Приклад:
#expanded_form(12) # return '10 + 2'
#expanded_form(42) # return '40 + 2'
#expanded_form(70304) # return '70000 + 300 + 4'

from typing import List


def expanded_form(num: int) -> str:
    num_str = str(num)
    length = len(num_str)

    result: List[str] = []

    for i, digit in enumerate(num_str):
        if digit != '0':

            result.append(digit + '0' * (length - i - 1))

    return ' + '.join(result)


print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))


def call_counter(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        result = func(*args, **kwargs)
        print(f'Функція {func.__name__} була запущена {count} раз(и)')
        return result

    return wrapper

@call_counter
def example_function():
    print("Функція виконується")

example_function()
example_function()
example_function()

