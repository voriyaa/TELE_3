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
            actions = {
                1: lambda: HandleUser.show_user_details(user),
                2: lambda: HandleUser.share_gb_with_friend(user),
                3: lambda: HandleUser.share_minute_with_friend(user),
                4: lambda: HandleUser.deposit_money(user),
                5: lambda: HandleUser.change_tariff(user),
                6: lambda: HandleUser.handle_buy_gb(user),
                7: lambda: HandleUser.handle_buy_minute(user),
                8: lambda: HandleUser.user_pay_tariff(user),
            }
            if variant == 0:
                return
            actions[variant]()

    @staticmethod
    def show_user_details(user):
        print(f"Остаток: {user.get_gb()}гб. | {user.get_minutes()}мин. | {user.get_balance()}руб.\n"
              f"Мой тариф: {user.get_tariff().get_gb()}гб. | {user.get_tariff().get_minutes()}мин. |"
              f" {user.get_tariff().get_cost_one_gb()}руб/гб. | {user.get_tariff().get_cost_one_minute()}руб/мин.")

    @staticmethod
    def share_gb_with_friend(user):
        HandleUser.__share_with_friend(user.share_gb, Constant.ENTER_SEND_GB)

    @staticmethod
    def share_minute_with_friend(user):
        HandleUser.__share_with_friend(user.share_minute, Constant.ENTER_SEND_MINUTE)

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
        HandleUser.__handle_buy_traffic(user, user.buy_gb, Constant.ENTER_VALUE_GB, "руб/гб")

    @staticmethod
    def handle_buy_minute(user):
        HandleUser.__handle_buy_traffic(user, user.buy_minute, Constant.ENTER_VALUE_MINUTE, "руб/мин")

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

    @staticmethod
    def __share_with_friend(share_function, message):
        phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
        while not database.find(UserAccount, (UserAccount.get_phone_number(UserAccount) == phone_number, True)):
            phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
        owner_of_number = database.get_object(UserAccount, (
            UserAccount.get_phone_number(UserAccount) == phone_number, True))

        value = GetCorrectValue.get_number(min_value=0,
                                           max_value=99999,
                                           first_out=message,
                                           second_out=Constant.ERROR)

        share_function(owner_of_number, value)
        database.insert(owner_of_number)

    @staticmethod
    def __handle_buy_traffic(user, buy_fucntion, input_message, output_message):
        value = GetCorrectValue.get_number(first_out=f"{input_message}"
                                                     f" {user.get_tariff().get_cost_one_gb()}{output_message}.?: ",
                                           second_out=Constant.ENTER_CORRECT_VALUE)
        print(buy_fucntion(value))
        database.insert(user)
