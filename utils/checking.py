from typing import Dict

from ticket.node import Node


class DataCheck:

    @classmethod
    def money_and_tickets(cls, input_data: Dict[int, Node], money: int) -> bool:
        summ = sum(list(ticket * node.count for ticket, node in input_data.items()))

        return summ >= money
