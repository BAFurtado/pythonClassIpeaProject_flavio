""" Protótipo do aplicativo de compensação de contas
"""


class IterHousehold(type):
    def __iter__(cls):
        return iter(cls._allHouseholds)


class Household(metaclass=IterHousehold):
    _allHouseholds = list()

    def __init__(self, name):
        self._allHouseholds.append(self)
        self.name = name
        self.size = 1
        self.expenditure = 0
        self.net = 0
        self.status = "even"

    def pay(self, value):
        self.expenditure += value
        # Household._allHouseholds += value

    def define_size(self, n):
        self.size = n

    # def get_total_families(self):
    #     pass

    def __repr__(self):
        return f'Family {self.name} has {self.size} people and paid {self.expenditure}'


def net_values():
    total_exp = 0
    for h in Household:
        total_exp += h.expenditure
    total_n = 0
    for h in Household:
        total_n += h.size
    unit_value = total_exp / total_n
    for h in Household:
        h.net = h.expenditure - h.size * unit_value
        if h.net > 0:
            h.status = "superavit"
            print(f'Family {h.name} must receive {h.net}')
        elif h.net < 0:
            h.status = "deficit"
            print(f'Family {h.name} must pay {h.net}')


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
    c = Household('Santos')
    c.define_size(2)

    for hh in Household:
        hh.pay(1000)
        print(hh)
        print(hh.expenditure)

    net_values()