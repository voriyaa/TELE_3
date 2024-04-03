from hashlib import sha256
from src.Admin.AdminAccount import AdminAccount, Tariff
from src.Constants.Constants import Constant
from src.Tools.DataBase import database
from src.Tools.GetInfo import GetInfo
from src.Tools.GetCorrectValue import GetCorrectValue
import os


def sha256_str(item):
    return sha256(str(item).encode()).hexdigest()


class AdminAuthorization:

    @staticmethod
    def admin_workflow():
        AdminAuthorization.verify_secret_key()

        variant = GetCorrectValue.get_number(min_value=0,
                                             max_value=2,
                                             first_out=Constant.CHOOSE_ACTIONS,
                                             second_out=Constant.CHOOSE_CORRECT_OPTION)
        if variant == 0:
            return
        elif variant == 1:
            return AdminAuthorization.create_admin_account()
        else:
            return AdminAuthorization.admin_login()

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
