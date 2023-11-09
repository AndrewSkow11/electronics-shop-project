"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


Item.pay_rate = 0.8


def test_aplay_discount():
    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000


# RESULTS
# ---------- coverage: platform darwin, python 3.11.3-final-0 ----------
# Name              Stmts   Miss  Cover
# -------------------------------------
# src/__init__.py       0      0   100%
# src/item.py          11      0   100%
# -------------------------------------
# TOTAL                11      0   100%
#
#
# =========================== 2 passed in 0.02s ============================


# homework 2


# длина наименования товара меньше 10 символов
def test_name_setter():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    item.name = '0123456789______________________________________'
    assert item.name == '0123456789'


def test_instantiate_from_csv():
    Item.instantiate_from_csv('items_for_test.csv')

    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам
    assert item1.name == 'Смартфон'

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

# results homework2
# ============================= test session starts ==============================
# collecting ... collected 5 items
#
# test_item.py::test_calculate_total_price PASSED                          [ 20%]
# test_item.py::test_aplay_discount PASSED                                 [ 40%]
# test_item.py::test_name_setter PASSED                                    [ 60%]
# test_item.py::test_instantiate_from_csv PASSED                           [ 80%]
# test_item.py::test_string_to_number PASSED                               [100%]
#
# ============================== 5 passed in 0.01s ===============================


