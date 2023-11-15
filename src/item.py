import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return f'{self.__name}'

    @name.setter
    def name(self, name):
        """Сеттер name проверяет, что длина наименования товара не больше 10 симвовов.
        В противном случае, обрезает строку (оставляет первые 10 символов)."""
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, path):
        """класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""
        cls.all = []
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = cls.string_to_number(row['quantity'])
                Item = cls(name, price, quantity)


    @staticmethod
    def string_to_number(string):
        """статический метод, возвращающий число из числа-строки"""
        return int(round(float(string), 1))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity*self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
