"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from _pytest.python_api import raises

from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_calcucate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    item1.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 5000.0


def test_instantiate_from_csv():
    assert type(Item.all) is list
    Item.all.clear()
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5.5') == 5
    with raises(Exception):
        Item.string_to_number('five')
    assert Item.string_to_number('6') == 6
    assert Item.string_to_number('9.8') == 9
