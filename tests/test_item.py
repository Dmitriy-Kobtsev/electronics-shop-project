"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src import item


def test_Item():
    item1 = item.Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20

    item.Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000