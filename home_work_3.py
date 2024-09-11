# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
# + сумма площин двох екземплярів ксласу
#  - різниця площин двох екземплярів ксласу
# == площин на рівність
# != площин на не рівність
# >, < меньше більше
# при виклику метода len() підраховувати сумму сторін

class Rectangle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def area(self) -> int:
        return self.x * self.y  # Площа прямокутника

    # Додавання площ
    def __add__(self, other: 'Rectangle') -> int:
        return self.area() + other.area()

    # Віднімання площ
    def __sub__(self, other: 'Rectangle') -> int:
        return self.area() - other.area()

    # Рівність площ
    def __eq__(self, other: 'Rectangle') -> bool:
        return self.area() == other.area()

    # Нерівність площ
    def __ne__(self, other: 'Rectangle') -> bool:
        return self.area() != other.area()

    # Менше
    def __lt__(self, other: 'Rectangle') -> bool:
        return self.area() < other.area()

    # Більше
    def __gt__(self, other: 'Rectangle') -> bool:
        return self.area() > other.area()

    # Метод len() для підрахунку суми сторін
    def __len__(self) -> int:
        return self.x + self.y


# Створюємо два прямокутники
rect1 = Rectangle(10, 20)
rect2 = Rectangle(5, 15)

# Додавання площ
print(f"Сума площ: {rect1 + rect2}")  # Виведе 275

# Різниця площ
print(f"Різниця площ: {rect1 - rect2}")  # Виведе 125

# Перевірка на рівність
print(f"Прямокутники рівні за площею? {rect1 == rect2}")  # False

# Перевірка на нерівність
print(f"Прямокутники не рівні за площею? {rect1 != rect2}")  # True

# Порівняння площ
print(f"rect1 більше за rect2? {rect1 > rect2}")  # True
print(f"rect1 менше за rect2? {rect1 < rect2}")  # False

# Сума сторін (len)
print(f"Сума сторін rect1: {len(rect1)}")  # Виведе 30

#############################################################
# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму

# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Cinderella(Human):
    count = 0

    def __init__(self, name: str, age: int, foot_size: int):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

class Prince(Human):
    def __init__(self, name: str, age: int, shoe_found: int):
        super().__init__(name, age)
        self.shoe_found = shoe_found

    def find_cinderella(self, cinderella_list: list):
        for cinderella in cinderella_list:
            if cinderella.foot_size == self.shoe_found:
                return cinderella
        return None

c1 = Cinderella("Cinderella1", 18, 37)
c2 = Cinderella("Cinderella2", 19, 38)
c3 = Cinderella("Cinderella3", 20, 37)

prince = Prince("Prince Charming", 25, 37)

found_cinderella = prince.find_cinderella([c1, c2, c3])

if found_cinderella:
    print(f"Found Cinderella: {found_cinderella.name}")
else:
    print("Cinderella not found.")

print(f"Number of Cinderella instances: {Cinderella.get_count()}")

#1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
#2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
#3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

from abc import ABC, abstractmethod
from typing import List

# 1. Абстрактний клас Printable
class Printable(ABC):
    @abstractmethod
    def print(self):
        """Абстрактний метод для виведення інформації."""
        pass

# 2. Класи Book та Magazine
class Book(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        print(f"Book: {self.name}")

class Magazine(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        print(f"Magazine: {self.name}")

# 3. Клас Main
class Main:
    printable_list: List[Printable] = []

    @classmethod
    def add(cls, item: Printable):
        """Додає екземпляри класів Book або Magazine до списку."""
        if isinstance(item, (Book, Magazine)):
            cls.printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        """Виводить всі журнали, викликаючи метод print."""
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        """Виводить всі книги, викликаючи метод print."""
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()

# Приклад використання
Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

print("Magazines:")
Main.show_all_magazines()
print('-' * 40)
print("Books:")
Main.show_all_books()






