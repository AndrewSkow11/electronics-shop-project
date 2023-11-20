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
    phone.quantity = 10
    assert 20 == phone + phone


def test_add_phone_raises(phone, smth):
    with pytest.raises(Exception):
        assert isinstance(smth, object)
        phone + smth

def test_number_of_sim_setter(phone):
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3


def test_setter_number_of_sim_raise():
    phone2 = Phone("Iphone 10", 200, 200, 1)

    with pytest.raises(TypeError):
        phone2.number_of_sim = "str"

    with pytest.raises(ValueError):
        phone2.number_of_sim = -23
        print(phone2.number_of_sim)


# ============================= test session starts ==============================
# collecting ... collected 5 items
#
# test_phone.py::test_init_ PASSED                                         [ 20%]
# test_phone.py::test_add_phone PASSED                                     [ 40%]
# test_phone.py::test_add_phone_raises PASSED                              [ 60%]
# test_phone.py::test_number_of_sim_setter PASSED                          [ 80%]
# test_phone.py::test_setter_number_of_sim_raise PASSED                    [100%]
#
# ============================== 5 passed in 0.01s ===============================
#
# Process finished with exit code 0