"""Модуль расчета количества билетов"""

import random
from collections import deque
from typing import Dict, Union
from .node import Node


class Calculate:
    """
    Клас для расчета количества номиналов для введенной сумы.
    Номиналы билетов выбираются из тех данных которые ввел пользователь.
    Выбор происходит рандомно.

    """

    def __init__(self, input_sum: int) -> None:

        self.summ = input_sum
        self.__graph = None
        self.data = None
        self.ticket = None
        self.previous_ticket = None
        self.last_ticket = None

        self.new_sum = 0
        self.searched = [0]

    @property
    def graph(self) -> Dict:
        return self.__graph

    @graph.setter
    def graph(self, data: Dict) -> None:
        self.__graph = {key: [node for node in data.keys() if node != key and data[key].count > 0] for key in data}

    @graph.getter
    def graph(self) -> Dict:
        return self.__graph

    def calculate(self, data: Dict[Union[int, str], Union[Node, str, int]]) -> Dict:
        """
        Метод расчета.

        Args:
            data: Данные указанные пользователем (номинал, стартовый номер и количество).

        Returns: input_data

        """

        self.graph = data
        self.data = data

        self.ticket = random.choice([key for key in self.data])
        if len(self.data) < 2:  # если пользователь указал только один номинал
            self.graph[self.ticket] = [self.ticket]

        search_deque = deque()  # создаем очередь
        search_deque += self.graph[self.ticket]  # добавляем

        while search_deque:
            self.ticket = search_deque.popleft()

            if self.data[self.ticket].count > 1 and self.ticket not in self.searched:

                if self.check_balance_new_sum():
                    self.new_sum -= self.last_ticket
                    self.data[self.last_ticket].taken_tickets = -1

                    self.searched[0] = self.last_ticket
                    self.last_ticket = self.previous_ticket

                    search_deque += self.graph[self.last_ticket]
                    continue

                if self.check_new_sum():
                    self.new_sum += self.ticket

                    self.data[self.ticket].taken_tickets = 1
                    self.data['sum_money'] = self.new_sum

                    return self.data

                else:
                    search_deque += self.graph[self.ticket]

                    self.new_sum += self.ticket
                    self.data[self.ticket].taken_tickets = 1

                    if self.previous_ticket is None:
                        self.previous_ticket = self.ticket

                    elif self.previous_ticket and self.last_ticket is None:
                        self.last_ticket = self.ticket

                    else:
                        self.previous_ticket = self.last_ticket
                        self.last_ticket = self.ticket

        self.data['sum_money'] = self.new_sum
        self.data['error'] = 'Ошибка работы расчета!\nПроверьте корректность ввода данных!'

        return self.data

    def check_new_sum(self) -> bool:
        """
        Метод делает проверку на равенство введенной суммы пользователем и новой расчетной суммы.

        Returns: bool

        """

        if (self.new_sum + self.ticket) == self.summ:
            return True

    def check_balance_new_sum(self) -> bool:

        if (self.new_sum + self.ticket) > self.summ:
            remainder = self.summ - self.new_sum

            if remainder in (key for key in self.data if self.data[key].count > 0):
                self.ticket = remainder
                return False

            # if self.ticket != self.last_ticket_key:
            remainderLast = self.summ - ((self.new_sum - self.last_ticket) + self.ticket)
            remainderPrevious = self.summ - ((self.new_sum - self.previous_ticket) + self.ticket)

            for key in self.data:
                if key == self.ticket and self.data[self.ticket].count < 2:
                    continue

                if key <= remainderLast and self.data[key].count > 0:
                    self.new_sum = remainderLast
                    self.data[self.last_ticket].taken_tickets = -1
                    self.last_ticket = self.ticket
                    self.data[self.ticket].taken_tickets = 1
                    self.ticket = key

                    return False

                if key <= remainderPrevious and self.data[key].count > 0:
                    self.new_sum = remainderPrevious
                    self.data[self.previous_ticket].taken_tickets = -1
                    self.previous_ticket = self.ticket
                    self.data[self.ticket].taken_tickets = 1
                    self.ticket = key

                    return False

            return True

        return False
