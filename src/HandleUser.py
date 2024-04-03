# -*- coding: utf-8 -*-
from UserAccount import UserAccount
from Constants import Constant
from Runner import database
from UserAccount import Tariff


class HandleUser(UserAccount):

    @staticmethod
    def handle_user_actions(user):
        while True:
            variant = input(Constant.SELECT_OPTION_OF_USER)
            while variant not in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
                print(Constant.CHOOSE_CORRECT_OPTION)
                variant = input(Constant.SELECT_OPTION_OF_USER)

            match variant:
                case '0':
                    return
                case '1':
                    HandleUser.show_user_details(user)
                case '2':
                    HandleUser.share_gb_with_friend(user)
                case '3':
                    HandleUser.share_minute_with_friend(user)
                case '4':
                    HandleUser.deposit_money(user)
                case '5':
                    HandleUser.change_tariff(user)
                case '6':
                    HandleUser.handle_buy_gb(user)
                case '7':
                    HandleUser.handle_buy_minute(user)
                case '8':
                    HandleUser.user_pay_tariff(user)
    
    @staticmethod
    def show_user_details(user):
        print(f"Остаток: {user.get_gb()}гб. | {user.get_minutes()}мин. | {user.get_balance()}руб.\n"
              f"Мой тариф: {user.get_tariff().get_gb()}гб. | {user.get_tariff().get_minutes()}мин. |"
              f" {user.get_tariff().get_cost_one_gb()}руб/гб. | {user.get_tariff().get_cost_one_minute()}руб/мин.")
    
    @staticmethod
    def share_gb_with_friend(user):
        phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
        while not database.find(UserAccount, UserAccount._UserAccount__phone_number == phone_number):
            phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
        owner_of_number = database.get_object(UserAccount, (
                UserAccount._UserAccount__phone_number == phone_number))

        how_many_gb = input(Constant.ENTER_SEND_GB_)
        if not how_many_gb.isdigit():
            print("Ошибка!")
            return

        print(user.share_gb(owner_of_number, how_many_gb))
        database.insert(owner_of_number)

    @staticmethod
    def share_minute_with_friend(user):
        phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
        while not database.find(UserAccount, UserAccount._UserAccount__phone_number == phone_number):
            phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
        owner_of_number = database.get_object(UserAccount, (
                UserAccount._UserAccount__phone_number == phone_number))
        how_many_minute = input(Constant.ENTER_SEND_MINUTE)
        if not how_many_minute.isdigit():
            print("Ошибка!")
            return

        user.share_minute(owner_of_number, how_many_minute)
        database.insert(owner_of_number)
    
    @staticmethod
    def deposit_money(user):
        amount = input(Constant.ENTER_AMOUNT)
        while not (amount.isdigit() and 0 < int(amount) < 10000):
            amount = input(Constant.ENTER_CORRECT_AMOUNT)

        user.deposit(int(amount))
        database.insert(user)
    
    @staticmethod
    def change_tariff(user):
        list_of_tariff = database.query(Tariff)
        HandleUser.display_tariffs(list_of_tariff)

        get_id = input(Constant.SELECT_TARIFF)
        while not get_id.isdigit():
            get_id = input(Constant.CHOOSE_CORRECT_OPTION_OF_SERVICES)

        tariff = database.get_object(Tariff, (Tariff.id == get_id))
        user.set_tariff(tariff)
        database.insert(user)

    @staticmethod
    def handle_buy_gb(user):
        value = input(f"{Constant.ENTER_VALUE_GB}"
                          f" {user.get_tariff().get_cost_one_gb()}руб/гб.?: ")
        while not value.isdigit():
            value = input(Constant.ENTER_CORRECT_VALUE)
        print(user.buy_gb(int(value)))
        database.insert(user)

    @staticmethod
    def handle_buy_minute(user):
        value = input(f"{Constant.ENTER_VALUE_MINUTE}"
                          f" {user.get_tariff().get_cost_one_minute()}руб/мин.?: ")
        while not value.isdigit():
            value = input(Constant.ENTER_CORRECT_VALUE)
        print(user.buy_minute(int(value)))
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
