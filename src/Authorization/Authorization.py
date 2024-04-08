# -*- coding: utf-8 -*-
from hashlib import sha256
from src.User.UserAccount import UserAccount
from src.Admin.AdminAccount import AdminAccount, Tariff
from src.Constants.Constants import AuthorizationConstants
from src.Tools.DataBase import database
from dotenv import load_dotenv
from src.Tools.GetCorrectValue import GetCorrectValue
from src.Tools.GetInfo import GetInfo
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
    def create_admin_account():
        info = GetInfo.preregistration() #TODO получать инфу от js

        admin = AdminAccount(
            info['first_name'], info['last_name'],
            info['birth_date'], info['passport_id'], info['sex'],
            info['username'], info['password'], info['phone_number']
        )
        database.insert(admin)
        return admin #TODO отправить класс AdminAccount js-у

    @staticmethod
    def admin_login():
        info_account = GetInfo.info_account() #TODO получаем инфу от js. надо менять

        if not database.find(AdminAccount, (AdminAccount.get_username(AdminAccount) == info_account['username'],
                                               AdminAccount.get_password(AdminAccount) == info_account[
                                                   'password'])):
            pass #TODO отправить js-у что нет такого пользователя с таким логином или паролем

        result = database.get_object(AdminAccount,
                                     (AdminAccount.get_username(AdminAccount) == info_account['username'],
                                      AdminAccount.get_password(AdminAccount) == info_account[
                                          'password']))
        return result #TODO нужно отправить профиль этого пользователя js-у

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
        print(AuthorizationConstants.LIST_SERVICES)
        for i, elem in enumerate(tariffs):
            print(
                f"{i + 1}: {elem.get_gb()}гб. | {elem.get_minutes()}мин. |"
                f" {elem.get_cost_one_gb()}руб/гб. "
                f"| {elem.get_cost_one_minute()}руб/мин. | {elem.get_price()}руб.")

    @staticmethod
    def choose_tariff_option(tariffs):
        option = input(AuthorizationConstants.SELECT_SERVICE)

        while not (
                option.isdigit() and
                (tariffs[0]).id <= int(option) <= (tariffs[tariffs.count() - 1]).id
        ):
            option = input(AuthorizationConstants.CHOOSE_VALID_OPTION_OF_SERVICES)
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
