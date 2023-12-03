"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item, InstantiateCSVError
import os
import pytest


def test_Item():
    item1 = Item("Смартфон", 10000, 20)

    assert str(item1) == 'Смартфон'
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

    assert item1.calculate_total_price() == 200000
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20

    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000

    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


    Item.instantiate_from_csv(os.path.join('src', 'Items.csv'))
    assert len(Item.all) == 5

def test_instantiate_csv_error():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(os.path.join('src', 'Items2.csv'))

def test_instantiate_from_csv_error():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('path')