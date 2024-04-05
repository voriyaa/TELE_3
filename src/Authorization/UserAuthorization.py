from hashlib import sha256
from src.User.UserAccount import UserAccount
from src.Constants.Constants import Constant
from src.Tools.DataBase import database
from src.Tools.GetInfo import GetInfo
from src.Tariffs.Tariff import Tariff
from src.Tools.GetCorrectValue import GetCorrectValue


def sha256_str(item):
    return sha256(str(item).encode()).hexdigest()


class UserAuthorization:

    @staticmethod
    def user_workflow():
        variant = GetCorrectValue.get_number(min_value=0,
                                             max_value=2,
                                             first_out=Constant.CHOOSE_ACTIONS,
                                             second_out=Constant.CHOOSE_CORRECT_OPTION)
        if variant == 0:
            return
        elif variant == 1:
            return UserAuthorization.create_user_account()
        else:
            return UserAuthorization.user_login()

    @staticmethod
    def create_user_account():
        info = GetInfo.preregistration()

        list_of_tariff = database.query(Tariff)
        UserAuthorization.display_tariffs(list_of_tariff)

        option = UserAuthorization.choose_tariff_option(list_of_tariff)

        user = UserAccount(
            info['first_name'], info['last_name'], info['birth_date'],
            info['passport_id'], info['sex'], info['username'],
            info['password'], info['phone_number'],
            list_of_tariff[option - 1]
        )
        database.insert(user)
        return user

    @staticmethod
    def display_tariffs(tariffs):
        print(Constant.LIST_SERVICES)
        for i, elem in enumerate(tariffs):
            print(
                f"{i + 1}: {elem.get_gb()}��. | {elem.get_minutes()}���. |"
                f" {elem.get_cost_one_gb()}���/��. "
                f"| {elem.get_cost_one_minute()}���/��. | {elem.get_price()}���.")

    @staticmethod
    def choose_tariff_option(tariffs):
        option = input(Constant.SELECT_SERVICE)

        while not (
                option.isdigit() and
                (tariffs[0]).id <= int(option) <= (tariffs[tariffs.count() - 1]).id
        ):
            option = input(Constant.CHOOSE_CORRECT_OPTION_OF_SERVICES)
        return int(option)

    @staticmethod
    def user_login():
        info_account = GetInfo.info_account()

        while not database.find(UserAccount, (UserAccount.get_username(UserAccount) == info_account['username'],
                                              UserAccount.get_password(UserAccount) == info_account['password'])):
            info_account = GetInfo.info_account()

        user = database.get_object(UserAccount, (UserAccount.get_username(UserAccount) == info_account['username'],
                                                 UserAccount.get_password(UserAccount) == info_account['password']))
        return user
