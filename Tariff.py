class Tariff:

    def __init__(self, cost_one_gb: int, cost_one_minute: int,
                 price: int, gb: int = 0, minute: int = 0,) -> None:
        self.__cost_one_gb = cost_one_gb
        self.__cost_one_minute = cost_one_minute
        self.__gb = gb
        self.__minute = minute
        self.__price = price

    def change_tariff(self, cost_one_gb: int, cost_one_minute: int,
                      price: int, gb: int = 0, minute: int = 0) -> None:
        self.__cost_one_gb = cost_one_gb
        self.__cost_one_minute = cost_one_minute
        self.__gb = gb
        self.__minute = minute
        self.__price = price

    def get_cost_one_gb(self) -> int:
        return self.__cost_one_gb

    def get_cost_one_minute(self) -> int:
        return self.__cost_one_minute

    def get_gb(self):
        return self.__gb

    def get_minutes(self):
        return self.__minute

    def get_price(self):
        return self.__price

