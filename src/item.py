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
            print(len(new_name))
            self.__name = new_name
        else:
            self.__name = new_name[:10]
            print(len(new_name))

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
            price = cls.string_to_number(item[1])
            quantity = cls.string_to_number(item[2])

            cls.all.append(Item(name, price, quantity))

            # for testing
            # print('item[0]', item[0])
            # print('item[1]', item[1])
            # print('item[2]', item[2])

            #cls.all.append( Item(item[0], float([1]), int(item[2]) ))

    @staticmethod
    def string_to_number(string_number):
        """статический метод, возвращающий число из числа-строки"""
        if '.' in string_number:
            return float(string_number)
        else:
            return int(string_number)





Item.instantiate_from_csv("items.csv")

print(Item.all[0].name)
print(Item.all[0].price)
print(Item.all[0].quantity)
