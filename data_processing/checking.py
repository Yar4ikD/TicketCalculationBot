from typing import Dict


class DataCheck:

    @classmethod
    def money_and_tickets(cls, input_data: Dict[int, list[int, int]], money: int) -> bool:
        summ = sum(list(ticket * val[1] for ticket, val in input_data.items()))

        return summ >= money
