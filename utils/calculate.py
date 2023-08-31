"""Модуль расчета количества номиналов билетов для заданной суммы денег."""

import random
from collections import deque
from typing import Dict, Union

from loggerSetup import loggers
from ticket.node import Node


class Calculate:
    """
    Класс для расчета введенной суммы из заранее заданных номиналов.
    Номиналы билетов выбираются из тех данных которые ввел пользователь.

    """

    def __init__(self, input_sum: int) -> None:
        """
        Конструктор класса.

        Args:
            input_sum: Сумма для расчета.

        """
        self.summ = input_sum
        self.__graph = None
        self.data = None
        self.ticket = None  # текущий узел, номинал билета
        self.previous_ticket = None  # предыдущий номинал
        self.last_ticket = None  # последний номинал

        self.new_sum = 0
        self.searched = [0]

    @property
    def graph(self) -> Dict:
        return self.__graph

    @graph.setter
    def graph(self, data: Dict) -> None:
        self.__graph = {
            key: [node for node in data.keys() if node != key and data[key].count > 0]
            for key in data
        }

    @graph.getter
    def graph(self) -> Dict:
        return self.__graph

    def calculate(
        self, data: Dict[Union[int, str], Union[Node, str, int]]
    ) -> Dict[Union[int, str], Union[Node, str]]:
        """
        Метод расчета.
        Для расчета суммы используется алгоритм обход графа: поиск в ширину (BFS).

        Args:
            data: Данные указанные пользователем (номиналы, стартовые номера и их количество).

        Returns: input_data

        """

        self.graph = data
        self.data = data

        self.ticket = random.choice([key for key in self.data])

        if len(self.data) < 2:  # если пользователь указал только один номинал
            self.graph[self.ticket] = [self.ticket]

        search_deque = deque()  # создаем очередь FIFO
        search_deque += self.graph[self.ticket]  # добавляем соседей узла

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

                if self.is_new_sum_equal_input_sum():
                    self.new_sum += self.ticket

                    self.data[self.ticket].taken_tickets = 1
                    self.data["sum_money"] = self.new_sum

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

        self.data["sum_money"] = self.new_sum
        self.data[
            "error"
        ] = "Ошибка работы расчета!\nПроверьте корректность ввода данных!"
        loggers.utils.warning(f"Ошибка расчета: sum - {self.summ}")
        return self.data

    def is_new_sum_equal_input_sum(self) -> bool:
        """
        Метод делает проверку на равенство введенной суммы пользователем
        и новой расчетной суммы.

        Returns: bool

        """

        if (self.new_sum + self.ticket) == self.summ:
            return True

    def check_balance_new_sum(self) -> bool:
        if (
            self.new_sum + self.ticket
        ) > self.summ:  # если новая сумма больше введенной суммы
            remainder = self.summ - self.new_sum

            if remainder in (key for key in self.data if self.data[key].count > 0):
                self.ticket = remainder
                return False

            remainder_last = self.summ - (
                (self.new_sum - self.last_ticket) + self.ticket
            )
            remainder_previous = self.summ - (
                (self.new_sum - self.previous_ticket) + self.ticket
            )

            for key in self.data:
                if key == self.ticket and self.data[self.ticket].count < 2:
                    continue

                if key <= remainder_last and self.data[key].count > 0:
                    self.new_sum = remainder_last
                    self.data[self.last_ticket].taken_tickets = -1
                    self.last_ticket = self.ticket
                    self.data[self.ticket].taken_tickets = 1
                    self.ticket = key

                    return False

                if key <= remainder_previous and self.data[key].count > 0:
                    self.new_sum = remainder_previous
                    self.data[self.previous_ticket].taken_tickets = -1
                    self.previous_ticket = self.ticket
                    self.data[self.ticket].taken_tickets = 1
                    self.ticket = key

                    return False

            return True

        return False
