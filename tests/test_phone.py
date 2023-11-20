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

def test_add_phone(phone, smth):
    assert phone + phone == 200


  def test_add_phone_raises():

        with pytest.raises(Exception) as excinfo:
            phone + smth.start_tasks_db('some/great/path', 'mysql')
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "db_type must be a 'tiny' or 'mongo'"

def test_number_of_sim_setter(phone):
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3
    phone.number: int = -2
    assert phone.number == -2
