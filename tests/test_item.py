"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src import item
import os


def test_Item():
    item1 = item.Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20

    item.Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000

    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'

    assert item.Item.string_to_number('5') == 5
    assert item.Item.string_to_number('5.0') == 5
    assert item.Item.string_to_number('5.5') == 5

    item.Item.instantiate_from_csv(os.path.join('src', 'Items.csv'))
    assert len(item.Item.all) == 5