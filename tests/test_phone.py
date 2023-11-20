import pytest
from src.phone import Phone
from tests.something import smth


@pytest.fixture
def phone():
    return Phone("Iphone 5s", 100, 100, 1)


def test_init_(phone):
    assert phone.name == "Iphone 5s"
    assert phone.price == 100
    assert phone.quantity == 100
    assert phone.number_of_sim == 1

def test_add_phone(phone):
    assert 200 == phone + phone


def test_add_phone_raises(phone, smth):
    with pytest.raises(Exception):
        phone + smth

def test_number_of_sim_setter(phone):
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3
    phone.number: int = -2
    assert phone.number == -2
