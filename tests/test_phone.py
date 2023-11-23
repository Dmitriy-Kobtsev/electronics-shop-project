from src.phone import Phone
from src.item import Item

def test_phone():
    phone1 = Phone("iPhone 15", 140_000, 5, 2)

    assert repr(phone1) == "Phone('iPhone 15', 140000, 5, 2)"
    assert phone1.number_of_sim == 2
    assert phone1.quantity == 5

    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10





