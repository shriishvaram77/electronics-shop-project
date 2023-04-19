import pytest
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_init():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2
    Phone.number_of_sim = 0
    assert 'Количество физических SIM-карт должно быть целым числом больше нуля.'
