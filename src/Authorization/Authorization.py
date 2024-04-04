from hashlib import sha256
from src.Admin.AdminAccount import AdminAccount, Tariff
from src.User.UserAccount import UserAccount
from src.Constants.Constants import Constant
from src.Tools.DataBase import database
from dotenv import load_dotenv
from src.Tools.GetInfo import GetInfo
from src.Tools.GetCorrectValue import GetCorrectValue
import os

def sha256_str(item):
    return sha256(str(item).encode()).hexdigest()


load_dotenv()

# DATABASE_URL = 'postgresql://postgres:123@192.168.0.105:5432/test'
"""db_file = 'example.db'

DATABASE_URL = f'sqlite:///{db_file}'

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)
s = session()
"""


class Authorization:

    @staticmethod
    def run():
        print(Constant.HI_TO_USER)

        variant = GetCorrectValue.get_number(min_value=1,
                                             max_value=2,
                                             first_out=Constant.CHOOSE_STATUS,
                                             second_out=Constant.CHOOSE_OPTION)

        if variant == 1:
            return Authorization.admin_workflow()
        else:
            return Authorization.user_workflow()

    @staticmethod
    def admin_workflow():
        Authorization.verify_secret_key()

        variant = GetCorrectValue.get_number(min_value=0,
                                             max_value=2,
                                             first_out=Constant.CHOOSE_ACTIONS,
                                             second_out=Constant.CHOOSE_CORRECT_OPTION)
        if variant == 0:
            return
        elif variant == 1:
            return Authorization.create_admin_account()
        else:
            return Authorization.admin_login()

    @staticmethod
    def verify_secret_key():
        key = input(Constant.ENTER_SECRET_KEY)
        while sha256_str(key) != os.getenv("SECRET_KEY"):
            key = input(Constant.WRONG_KEY)

    @staticmethod
    def create_admin_account():
        info = GetInfo.preregistration()

        admin = AdminAccount(
            info['first_name'], info['last_name'],
            info['birth_date'], info['passport_id'], info['sex'],
            info['username'], info['password'], info['phone_number']
        )
        database.insert(admin)
        return admin

    @staticmethod
    def admin_login():
        info_account = GetInfo.info_account()

        while not database.find(AdminAccount, (AdminAccount.get_username(AdminAccount) == info_account['username'],
                                               AdminAccount.get_password(AdminAccount) == info_account['password'])):
            print(Constant.INCORRECT_LOGIN_PASSWORD)
            info_account = GetInfo.info_account()

        result = database.get_object(AdminAccount, (AdminAccount.get_username(AdminAccount) == info_account['username'],
                                                    AdminAccount.get_password(AdminAccount) == info_account[
                                                        'password']))
        return result

    @staticmethod
    def user_workflow():
        variant = GetCorrectValue.get_number(min_value=0,
                                             max_value=2,
                                             first_out=Constant.CHOOSE_ACTIONS,
                                             second_out=Constant.CHOOSE_CORRECT_OPTION)
        if variant == 0:
            return
        elif variant == 1:
            return Authorization.create_user_account()
        else:
            return Authorization.user_login()

    @staticmethod
    def create_user_account():
        info = GetInfo.preregistration()

        list_of_tariff = database.query(Tariff)
        Authorization.display_tariffs(list_of_tariff)

        option = Authorization.choose_tariff_option(list_of_tariff)

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
                f"{i + 1}: {elem.get_gb()}ГБ. | {elem.get_minutes()}мин. |"
                f" {elem.get_cost_one_gb()}руб/гб. "
                f"| {elem.get_cost_one_minute()}руб/гб. | {elem.get_price()}руб.")

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
