from src.User.UserAccount import UserAccount, Tariff
from src.Authorization.Authorization import database
from flask_jwt_extended import create_access_token
from datetime import timedelta
from src.Tools.MyHashFunc import sha256


class HandleUser(UserAccount):
    @staticmethod
    def get_token(user, expire_time=24):
        expire_delta = timedelta(expire_time)
        token = create_access_token(
            identity=user.get_username(), expires_delta=expire_delta, additional_claims={'role': 'user'})
        return token

    @staticmethod
    def create_user_account(**kwargs):
        tariff = database.get_object(Tariff, (Tariff.id == kwargs['tariff_id'], True))
        kwargs.pop('tariff_id')
        kwargs['main_tariff'] = tariff
        user = UserAccount(**kwargs)
        database.insert(user)
        return HandleUser.get_token(user)

    @staticmethod
    def show_user_details(username):
        user = database.get_object(UserAccount, (UserAccount.get_username(UserAccount) == username, True))
        data = {}
        data['user_minutes'] = user.get_minutes()
        data['balance'] = user.get_balance()
        data['user_gbs'] = user.get_gb()
        data['gb'] = user.get_tariff().get_gb()
        data['minute'] = user.get_tariff().get_minutes()
        data['cost_one_minute'] = user.get_tariff().get_cost_one_minute()
        data['cost_one_gb'] = user.get_tariff().get_cost_one_gb()
        data['price'] = user.get_tariff().get_price()
        return data

    @staticmethod
    def share_gb_with_friend(username, phone_number, value):
        user = database.get_object(UserAccount, (UserAccount.get_password(UserAccount) == username, True))
        if user is None:
            return None
        if user.get_gb() <= value:
            return False
        if HandleUser.__share_with_friend(user.share_gb, phone_number, value) is None:
            return None
        database.insert(user)
        return True

    @staticmethod
    def share_minute_with_friend(username, phone_number, value):
        user = database.get_object(UserAccount, (UserAccount.get_password(UserAccount) == username, True))
        if user is None:
            return None
        if user.get_minutes() <= value:
            return False
        if HandleUser.__share_with_friend(user.share_minute, phone_number, value) is None:
            return None
        database.insert(user)
        return True

    @staticmethod
    def deposit_money(username, value):
        amount = GetCorrectValue.get_number(min_value=1,
                                            max_value=10000,
                                            first_out=UserConstants.ENTER_AMOUNT,
                                            second_out=UserConstants.ENTER_VALID_AMOUNT)
        user.deposit(amount)
        database.insert(user)

    @staticmethod
    def change_tariff(user):
        list_of_tariff = database.query(Tariff)
        HandleUser.display_tariffs(list_of_tariff)

        get_id = GetCorrectValue.get_number(max_value=10000,
                                            first_out=UserConstants.SELECT_TARIFF,
                                            second_out=UserConstants.CHOOSE_VALID_OPTION_OF_SERVICES)

        tariff = database.get_object(Tariff, (Tariff.id == get_id, True))
        user.set_tariff(tariff)
        database.insert(user)

    @staticmethod
    def handle_buy_gb(user):
        HandleUser.__handle_buy_traffic(user, user.buy_gb, UserConstants.ENTER_VALUE_GB, "руб/гб")

    @staticmethod
    def handle_buy_minute(user):
        HandleUser.__handle_buy_traffic(user, user.buy_minute, UserConstants.ENTER_VALUE_MINUTE, "руб/мин")

    @staticmethod
    def user_pay_tariff(user):
        print(user.pay_tariff())
        database.insert(user)

    @staticmethod
    def display_tariffs(tariffs):
        print(UserConstants.LIST_SERVICES)
        for i, elem in enumerate(tariffs):
            print(
                f"{i + 1}: {elem.get_gb()}ГБ. | {elem.get_minutes()}мин. |"
                f" {elem.get_cost_one_gb()}руб/гб. "
                f"| {elem.get_cost_one_minute()}руб/гб. | {elem.get_price()}руб.")

    @staticmethod
    def __share_with_friend(share_function, phone_number, value):
        owner_of_number = database.get_object(UserAccount, (
            UserAccount.get_phone_number(UserAccount) == phone_number, True))
        if owner_of_number is None:
            return None
        share_function(owner_of_number, value)
        database.insert(owner_of_number)
        return True

    @staticmethod
    def __handle_buy_traffic(user, buy_function, input_message, output_message):
        value = GetCorrectValue.get_number(first_out=f"{input_message}"
                                                     f" {user.get_tariff().get_cost_one_gb()}{output_message}.?: ",
                                           second_out=UserConstants.ENTER_VALID_VALUE)
        print(buy_function(value))
        database.insert(user)

    @staticmethod
    def is_user(methods, attribute):
        getter = {'username': UserAccount.get_username,
                  'passport_id': UserAccount.get_passport_id,
                  'phone_number': UserAccount.get_phone_number
                  }
        return database.find(UserAccount, (getter[methods](UserAccount) == attribute, True))