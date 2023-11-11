import pytest
from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)


def test_calculate_total_price(item1, item2):
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


Item.pay_rate = 0.8


def test_aplay_discount(item1, item2):
    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000

# длина наименования товара меньше 10 символов
def test_name_setter():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    item.name = '0123456789______________________________________'
    assert item.name == '0123456789'


def test_instantiate_from_csv(item1):
    Item.instantiate_from_csv('items_for_test.csv')
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

# home work 3

def test_repr(item1, item2):
    assert item1.__repr__() == "Item('Смартфон', 10000, 20)"
    assert item2.__repr__() == "Item('Ноутбук', 20000, 5)"


def test_str(item1, item2):
    assert item1.__str__() == "Смартфон"
    assert item2.__str__() == "Ноутбук"

# ============================= test session starts ==============================
# collecting ... collected 7 items
#
# test_item.py::test_calculate_total_price PASSED                          [ 14%]
# test_item.py::test_aplay_discount PASSED                                 [ 28%]
# test_item.py::test_name_setter PASSED                                    [ 42%]
# test_item.py::test_instantiate_from_csv PASSED                           [ 57%]
# test_item.py::test_string_to_number PASSED                               [ 71%]
# test_item.py::test_repr PASSED                                           [ 85%]
# test_item.py::test_str PASSED                                            [100%]
#
# ============================== 7 passed in 0.01s ===============================
#
# Process finished with exit code 0
