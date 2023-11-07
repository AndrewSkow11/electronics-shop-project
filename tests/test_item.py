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
