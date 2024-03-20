from sqlalchemy import Column, Integer
from BaseUser import Base


class Tariff(Base):

    id = Column(Integer, primary_key=True)

    def __init__(self, cost_one_gb: int, cost_one_minute: int,
                 price: int, gb: int = 0, minute: int = 0, ) -> None:
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

    __tablename__ = 'tariff'
    __cost_one_gb = Column(Integer, unique=False, nullable=True)
    __cost_one_minute = Column(Integer, unique=False, nullable=True)
    __gb = Column(Integer, unique=False, nullable=True)
    __minute = Column(Integer, unique=False, nullable=True)
    __price = Column(Integer, unique=False, nullable=True)

