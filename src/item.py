# homework 2 status
import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    # добавим объекты из csv_file
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        # сделали атрибут name приватным
        self.__name = name
        self.price = price
        self.quantity = quantity

    # assert repr(item1) == "Item('Смартфон', 10000, 20)"
    # assert str(item1) == 'Смартфон'

    # home_work 3
    def __repr__(self):
        return f"{Item.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name



    # добавление геттеров и сеттеров
    # геттер
    @property
    def name(self):
        return self.__name

    # сеттер
    @name.setter
    def name(self, new_name):
        """в сеттере name проверять, что длина наименования товара не больше
        10 симвовов. В противном случае, обрезать строку (оставить первые 10
        символов)."""

        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename):
        """класс-метод, инициализирующий экземпляры класса Item
        данными из файла src/items.csv"""

        list_of_items = []

        with (open(filename, newline='', encoding='windows-1251') as csvfile):
            content = csv.reader(csvfile)
            for line in content:
                list_of_items.append(line)

        del list_of_items[0]  # удаляем заголовочную строку

        for item in list_of_items:

            name = item[0]
            price = float(item[1])
            quantity = cls.string_to_number(item[2])

            cls.all.append(Item(name, price, quantity))

    @staticmethod
    def string_to_number(string_number):
        """статический метод, возвращающий число из числа-строки"""
        # к int судя по тестам
        if '.' in string_number:
            return int(float(string_number))
        else:
            return int(string_number)

    def __add__(self, other):
        if (other.__class__.__name__ == "Phone"
                or other.__class__.__name__ == "Item"):
            return self.quantity + other.quantity
        else:
            raise Exception("Фатальная ошибка, несовместимые типы данных")