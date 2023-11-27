import pytest
import os
from src.item import Item, InstantiateCSVError
from tests.something import Something
# from src.instantiate_csv_error import InstantiateCSVError

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
    # file_relative_path = "items_for_test.csv"
    # file_abs_path = os.path.abspath(file_relative_path)
    # file_for_coverage = 'tests/items_for_test.csv'

    Item.instantiate_from_csv('items_for_test.csv')  # ??
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам
    assert item1.name == 'Смартфон'

    # print('\nАбсолютный путь:', file_abs_path)


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


@pytest.fixture
def smth_random_class():
    return Something(5)


def test_add_phone_raises(item1, smth_random_class):
    with pytest.raises(Exception):
        # assert isinstance(smth_random_class, object)
        item1 + smth_random_class()


# for homework 6
def test_not_exist_file():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('this_file_exists_only_in_your_head')

    with pytest.raises(FileNotFoundError, match='Отсутствует файл items.csv'):
        Item.instantiate_from_csv('one_more_strange_file')

def test_incorrect_file():
    with pytest.raises(InstantiateCSVError, match='Файл item.csv поврежден'):
        Item.instantiate_from_csv('incorrect_file.csv')

# RESULTS

# ============================= test session starts ==============================
# collecting ... collected 10 items
#
# test_item.py::test_calculate_total_price PASSED                          [ 10%]
# test_item.py::test_aplay_discount PASSED                                 [ 20%]
# test_item.py::test_name_setter PASSED                                    [ 30%]
# test_item.py::test_instantiate_from_csv PASSED                           [ 40%]
# test_item.py::test_string_to_number PASSED                               [ 50%]
# test_item.py::test_repr PASSED                                           [ 60%]
# test_item.py::test_str PASSED                                            [ 70%]
# test_item.py::test_add_phone_raises PASSED                               [ 80%]
# test_item.py::test_not_exist_file PASSED                                 [ 90%]
# test_item.py::test_incorrect_file PASSED                                 [100%]
#
# ============================== 10 passed in 0.01s ==============================
#
# Process finished with exit code 0
