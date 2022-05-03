""" Protótipo do aplicativo de compensação de contas
"""


class IterHousehold(type):
    def __iter__(cls):
        return iter(cls._allHouseholds)


class Household(metaclass=IterHousehold):
    _allHouseholds = []

    def __init__(self, name):
        self._allHouseholds.append(self)
        self.name = name
        self.size = 1
        self.expenditure = 0
        self.net = 0
        self.status = 0

    def pay(self, value):
        self.expenditure += value

    def define_size(self, n):
        self.size = n

    def __repr__(self):
        return f'Family {self.name} has {self.size} people and paid {self.expenditure}'


if __name__ == '__main__':
    a = Household('Silva')
    a.define_size(2)
    b = Household('Costa')
    b.define_size(4)
    print(a)
    print(b)
    a.pay(200)
    b.pay(500)
    print(a)
    print(b)

    for hh in Household:
        hh.pay(1000)
        print(hh)