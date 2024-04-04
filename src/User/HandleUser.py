# -*- coding: utf-8 -*-
from src.User.UserAccount import UserAccount
from src.Constants.Constants import Constant
from src.Authorization.Authorization import database
from src.User.UserAccount import Tariff
from src.Tools.GetCorrectValue import GetCorrectValue


class HandleUser(UserAccount):

    @staticmethod
    def handle_user_actions(user):
        while True:
            variant = GetCorrectValue.get_number(min_value=0,
                                                 max_value=8,
                                                 first_out=Constant.SELECT_OPTION_OF_USER,
                                                 second_out=Constant.SELECT_CORRECT_OPTION_OF_USER)
            match variant:
                case 0:
                    return
                case 1:
                    HandleUser.show_user_details(user)
                case 2:
                    HandleUser.share_gb_with_friend(user)
                case 3:
                    HandleUser.share_minute_with_friend(user)
                case 4:
                    HandleUser.deposit_money(user)
                case 5:
                    HandleUser.change_tariff(user)
                case 6:
                    HandleUser.handle_buy_gb(user)
                case 7:
                    HandleUser.handle_buy_minute(user)
                case 8:
                    HandleUser.user_pay_tariff(user)

    @staticmethod
    def show_user_details(user):
        print(f"Остаток: {user.get_gb()}гб. | {user.get_minutes()}мин. | {user.get_balance()}руб.\n"
              f"Мой тариф: {user.get_tariff().get_gb()}гб. | {user.get_tariff().get_minutes()}мин. |"
              f" {user.get_tariff().get_cost_one_gb()}руб/гб. | {user.get_tariff().get_cost_one_minute()}руб/мин.")

    @staticmethod
    def share_gb_with_friend(user):
        phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
        while not database.find(UserAccount, (UserAccount.get_phone_number(UserAccount) == phone_number, True)):
            phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
        owner_of_number = database.get_object(UserAccount, (
                UserAccount.get_phone_number(UserAccount) == phone_number, True))

        how_many_gb = GetCorrectValue.get_number(min_value=0,
                                                 max_value=99999,
                                                 first_out=Constant.ENTER_SEND_GB,
                                                 second_out=Constant.ERROR)

        print(user.share_gb(owner_of_number, how_many_gb))
        database.insert(owner_of_number)

    @staticmethod
    def share_minute_with_friend(user):
        phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
        while not database.find(UserAccount, (UserAccount.get_phone_number(UserAccount) == phone_number, True)):
            phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
        owner_of_number = database.get_object(UserAccount, (
            UserAccount.get_phone_number(UserAccount) == phone_number, True))

        how_many_minute = GetCorrectValue.get_number(min_value=0,
                                                     max_value=99999,
                                                     first_out=Constant.ENTER_SEND_MINUTE,
                                                     second_out=Constant.ERROR)

        user.share_minute(owner_of_number, how_many_minute)
        database.insert(owner_of_number) \


    @staticmethod
    def deposit_money(user):
        amount = GetCorrectValue.get_number(min_value=1,
                                            max_value=10000,
                                            first_out=Constant.ENTER_AMOUNT,
                                            second_out=Constant.ENTER_CORRECT_AMOUNT)
        user.deposit(amount)
        database.insert(user)

    @staticmethod
    def change_tariff(user):
        list_of_tariff = database.query(Tariff)
        HandleUser.display_tariffs(list_of_tariff)

        get_id = GetCorrectValue.get_number(max_value=10000,
                                            first_out=Constant.SELECT_TARIFF,
                                            second_out=Constant.CHOOSE_CORRECT_OPTION_OF_SERVICES)

        tariff = database.get_object(Tariff, (Tariff.id == get_id, True))
        user.set_tariff(tariff)
        database.insert(user)

    @staticmethod
    def handle_buy_gb(user):
        value = GetCorrectValue.get_number(first_out=f"{Constant.ENTER_VALUE_GB}"
                                                     f" {user.get_tariff().get_cost_one_gb()}руб/гб.?: ",
                                           second_out=Constant.ENTER_CORRECT_VALUE)
        print(user.buy_gb(value))
        database.insert(user)

    @staticmethod
    def handle_buy_minute(user):
        value = GetCorrectValue.get_number(first_out=f"{Constant.ENTER_VALUE_MINUTE}"
                                                     f" {user.get_tariff().get_cost_one_minute()}руб/мин.?: ",
                                           second_out=Constant.ENTER_CORRECT_VALUE)
        print(user.buy_minute(value))
        database.insert(user)

    @staticmethod
    def user_pay_tariff(user):
        print(user.pay_tariff())
        database.insert(user)

    @staticmethod
    def display_tariffs(tariffs):
        print(Constant.LIST_SERVICES)
        for i, elem in enumerate(tariffs):
            print(
                f"{i + 1}: {elem.get_gb()}ГБ. | {elem.get_minutes()}мин. |"
                f" {elem.get_cost_one_gb()}руб/гб. "
                f"| {elem.get_cost_one_minute()}руб/гб. | {elem.get_price()}руб.")
