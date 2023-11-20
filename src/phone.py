from src.item import Item

class Phone(Item):
    """Phone содержит все атрибуты класса Item и дополнительно атрибут,
     содержащий количество поддерживаемых сим-карт"""
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __str__(self):
        return self.name

    def __repr__(self):
        return (f"{Phone.__name__}('{self.name}', {self.price},"
                f" {self.quantity}, {self.__number_of_sim})")

    # реализуйте возможность сложения экземпляров класса
    # Phone и Item (сложение по количеству товара в магазине)

    # Реализуйте проверки, чтобы нельзя было сложить Phone или Item
    # с экземплярами не Phone или Item классов.

    def __add__(self, other):
        if (other.__class__.__name__ == "Phone"
                or other.__class__.__name__ == "Item"):
            return self.quantity + other.quantity
        else:
            raise Exception("Фатальная ошибка, несовместимые типы данных")

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value > 0 and isinstance(value, int):
            self.__number_of_sim = value
        else:
            raise ValueError("Количество физических SIM-карт"
                              " должно быть целым числом больше нуля")



# phone = Phone('Smth', 200, 2, 2)
# phone.number_of_sim = 0