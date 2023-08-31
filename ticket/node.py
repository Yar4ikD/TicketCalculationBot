class Node:
    """
    Клас номинал билета.

    """

    def __init__(self, denomination: int) -> None:
        """
        Конструктор класса.

        Args:
            denomination: Номинал билета.

        """
        self.denomination = denomination
        self.__count = 0
        self.__startNumber = 0
        self.__taken_tickets = 0

    @property
    def count(self) -> int:
        """
        Метод возвращает количество билета.

        Returns: __count

        """
        return self.__count

    @count.setter
    def count(self, val: int) -> None:
        self.__count = val

    @property
    def start_number(self) -> int:
        """
        Метод возвращает начальный номер билета.

        Returns: __startNumber

        """
        return self.__startNumber

    @start_number.setter
    def start_number(self, val):
        self.__startNumber = val

    @property
    def taken_tickets(self) -> int:
        """
        Метод возвращает кол-во взятых билетов данного номинала, для расчета.

        Returns: __taken_tickets

        """
        return self.__taken_tickets

    @taken_tickets.setter
    def taken_tickets(self, value) -> None:
        self.__count -= value
        self.__taken_tickets += value

    @property
    def taken_sum(self) -> int:
        """
        Метод возвращает сумму кол-ва билетов данного номинала,
        которые было использовано для расчета.

        Returns: taken_tickets * denomination

        """
        return self.taken_tickets * self.denomination

    @property
    def left(self) -> int:
        """
        Метод возвращает кол-во оставшихся билетов.

        Returns: count

        """
        return self.count

    @property
    def left_sum(self) -> int:
        return self.count * self.denomination

    @property
    def end_number(self) -> int:
        """
        Метод возвращает конечный номер билета.

        Returns: __startNumber + __taken_tickets

        """
        return self.__startNumber + self.__taken_tickets
