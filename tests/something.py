import pytest


class Something():
    def __init__(self, number_of_sim):
        self.number_of_sim = number_of_sim


@pytest.fixture
def smth():
    return Something(3)
