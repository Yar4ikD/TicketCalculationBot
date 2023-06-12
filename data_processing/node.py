
class Node:
    def __init__(self, denomination: int):
        self.denomination = denomination
        self.__count = 0
        self.__startNumber = 0
        self.__taken_tickets = 0

    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, val):
        self.__count = val

    @property
    def start_number(self) -> int:
        return self.__startNumber

    @start_number.setter
    def start_number(self, val):
        self.__startNumber = val

    @property
    def taken_tickets(self):
        return self.__taken_tickets

    @taken_tickets.setter
    def taken_tickets(self, value):
        self.__count -= value
        self.__taken_tickets += value

    @property
    def taken_sum(self):
        return self.taken_tickets * self.denomination

    @property
    def left(self):
        return self.count

    @property
    def left_sum(self):
        return self.count * self.denomination

    @property
    def end_number(self):
        return self.__startNumber + self.__taken_tickets
