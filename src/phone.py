from src.item import Item

class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{super().__repr__()[:-1]}, {self.__number_of_sim})"

    def __add__(self, other):
        if not isinstance(other, Phone) or not isinstance(other, Item):
            raise ValueError
        else:
            return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")



