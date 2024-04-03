from sqlalchemy import ForeignKey

from src.BaseUser.BaseUser import BaseUser, Column, String, Integer
from sqlalchemy.orm import relationship
from src.Tariffs.Tariff import Tariff


class UserAccount(BaseUser):

    id = Column(Integer, primary_key=True)
    tariff_id = Column(Integer, ForeignKey('tariff.id'))

    def __init__(self, first_name: str, last_name: str, birth_date: str,
                 passport_id: int, sex: str, username: str, password: str,
                 phone_number: str, main_tariff: Tariff) -> None:
        super().__init__(first_name, last_name, birth_date, passport_id, sex)
        self.__username = username
        self.__password = password
        self.__phone_number = phone_number
        self.__gb = 0
        self.__minutes = 0
        self.__balance = 0
        self.__main_tariff = main_tariff

    def get_username(self) -> str:
        return self.__username

    def get_password(self) ->str:
        return self.__password

    def get_phone_number(self) -> str:
        return self.__phone_number

    def get_gb(self) -> int:
        return self.__gb

    def set_gb(self, value: int) -> None:
        self.__gb = value

    def get_minutes(self) -> int:
        return self.__minutes

    def set_minutes(self, value: int) -> None:
        self.__minutes = value

    def get_balance(self) -> int:
        return self.__balance

    def set_balance(self, value: int) -> None:
        self.__balance = value

    def share_gb(self, other, value: int) -> str:
        if self.get_gb() >= value:
            other.set_gb(other.get_gb() + value)
            self.set_gb(self.get_gb() - value)
            return "Успешно!"
        else:
            return "Недостаточно гигабайтов на балансе"

    def share_minute(self, other, value: int) -> str:
        if self.get_minutes() >= value:
            other.set_minutes(other.get_minutes() + value)
            self.set_minutes(self.get_minutes() - value)
            return "Успешно!"
        else:
            return "Недостаточно минут на балансе"

    def deposit(self, money: int) -> None:
        self.set_balance(self.get_balance() + money)

    def get_tariff(self) -> Tariff:
        return self.__main_tariff

    def pay_tariff(self):
        if self.get_tariff().get_price() >= self.get_balance():
            return "Недостаточно денег на балансе, пополните пожалуйста ваш баланс"
        self.set_gb(self.get_gb() + self.get_tariff().get_gb())
        self.set_minutes(self.get_minutes() + self.get_tariff().get_minutes())
        self.set_balance(self.get_balance() - self.get_tariff().get_price())
        return "Успешно!"

    def set_tariff(self, new_tariff: Tariff) -> None:
        self.__main_tariff = new_tariff

    def buy_gb(self, value: int) -> str:
        if self.get_balance() >= self.get_tariff().get_cost_one_gb() * value:
            self.set_gb(self.get_gb() + value)
            self.set_balance(self.get_balance() - self.get_tariff().get_cost_one_gb() * value)
            return "Успешно!"
        else:
            return "Недостаточно денег на балансе"

    def buy_minute(self, value: int) -> str:
        if self.get_balance() >= self.get_tariff().get_cost_one_minute() * value:
            self.set_minutes(self.get_minutes() + value)
            self.set_balance(self.get_balance() - self.get_tariff().get_cost_one_minute() * value)
            return "Успешно!"
        else:
            return "Недостаточно денег на балансе"

    def change_number(self, new_number: str) -> None:
        self.__phone_number = new_number


    __username = Column(String(1000), unique=True)
    __password = Column(String(1000), unique=False)
    __phone_number = Column(String(15), unique=True)
    __gb = Column(Integer, unique=False, nullable=True)
    __minutes = Column(Integer, unique=False, nullable=True)
    __balance = Column(Integer, unique=False, nullable=True)
    __main_tariff = relationship("Tariff")
    __tablename__ = 'user_account'
