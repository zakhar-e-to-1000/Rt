from math import inf
KOEFITIENTS = {'bosh':556, 'Руці-Лапки': 1}

class DishWasher:
    def __init__(self, mark) -> None:
        self.count = 0
        self.__mark = mark
    def wash(self):
        self.count += 1
    def spent_cost(self):
        return self.count*KOEFITIENTS.get(self._mark, inf)

d = DishWasher("hh")
print(d.__mark)