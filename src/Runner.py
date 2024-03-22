from hashlib import sha256
from AdminAccount import AdminAccount, Tariff
from UserAccount import UserAccount
from Constants import Constant
from DataBase import database


def sha256_str(item):
    return sha256(str(item).encode()).hexdigest()


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
        variant = Authorization.get_variant()

        if variant == 1:
            return Authorization.admin_workflow()
        else:
            return Authorization.user_workflow()

    @staticmethod
    def get_variant():
        variant = int(input(Constant.CHOOSE_STATUS))
        while variant not in [1, 2]:
            variant = int(input(Constant.CHOOSE_OPTION_1))
        return variant

    @staticmethod
    def admin_workflow():
        Authorization.verify_secret_key()

        variant = Authorization.choose_admin_option()
        if variant == 0:
            Authorization.run()
            return
        elif variant == 1:
            return Authorization.create_admin_account()
        else:
            return Authorization.admin_login()

    @staticmethod
    def choose_admin_option():
        variant = int(input(Constant.CHOOSE_OPTION_2))
        while variant not in [0, 1, 2]:
            variant = int(input(Constant.CHOOSE_CORRECT_OPTION))
        return variant

    @staticmethod
    def verify_secret_key():
        key = input(Constant.ENTER_SECRET_KEY)
        while sha256_str(key) != Constant.SECRET_KEY:
            key = input(Constant.WRONG_KEY)

    @staticmethod
    def create_admin_account():
        first_name = input(Constant.ENTER_NAME)
        last_name = input(Constant.ENTER_SURNAME)
        birth_date = input(Constant.ENTER_BIRTH_DATE)
        sex = input(Constant.ENTER_YOUR_SEX)
        passport_id = int(input(Constant.ENTER_PASSPORT_ID))
        phone_number = input(Constant.ENTER_PHONE_NUMBER)
        username = input(Constant.ENTER_USERNAME)
        password = input(Constant.ENTER_PASSWORD)

        admin = AdminAccount(first_name, last_name, birth_date, passport_id, sex,
                             username, password, phone_number)

        database.insert(admin)
        return admin

    @staticmethod
    def admin_login():
        username = input(Constant.ENTER_USERNAME)
        password = sha256_str(input(Constant.ENTER_PASSWORD))

        while database.find(AdminAccount, (AdminAccount._AdminAccount__username == username and
                                           AdminAccount._AdminAccount__password == password)):
            print(Constant.INCORRECT_LOGIN_PASSWORD)
            username = input(Constant.ENTER_USERNAME)
            password = sha256_str(input(Constant.ENTER_PASSWORD))
        result = database.get_object(AdminAccount, (AdminAccount._AdminAccount__username == username and
                                                    AdminAccount._AdminAccount__password == password))
        return result[0]

    @staticmethod
    def user_workflow():
        variant = Authorization.choose_user_option()

        if variant == 0:
            Authorization.run()
            return
        elif variant == 1:
            return Authorization.create_user_account()
        else:
            return Authorization.user_login()

    @staticmethod
    def choose_user_option():
        variant = int(input(Constant.CHOOSE_OPTION_2))
        while variant not in [0, 1, 2]:
            variant = int(input(Constant.CHOOSE_OPTION_1))
        return variant

    @staticmethod
    def create_user_account():
        first_name = input(Constant.ENTER_NAME)
        last_name = input(Constant.ENTER_SURNAME)
        birth_date = input(Constant.ENTER_BIRTH_DATE)
        sex = input(Constant.ENTER_YOUR_SEX)
        passport_id = int(input(Constant.ENTER_PASSPORT_ID))
        phone_number = input(Constant.ENTER_PHONE_NUMBER)
        username = input(Constant.ENTER_USERNAME)
        password = sha256_str(input(Constant.ENTER_PASSWORD))

        list_of_tariff = database.query(Tariff)
        Authorization.display_tariffs(list_of_tariff)

        option = Authorization.choose_tariff_option(list_of_tariff)

        user = UserAccount(first_name, last_name, birth_date, passport_id, sex,
                           username, password, phone_number,
                           list_of_tariff[option - 1])
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
        option = int(input(Constant.CHOOSE_OPTION_4))
        while not (
                (tariffs[0]).id <= option <= (tariffs[tariffs.count() - 1]).id):
            option = int(input(Constant.CHOOSE_CORRECT_OPTION_2))
        return option

    @staticmethod
    def user_login():
        username = input(Constant.ENTER_USERNAME)
        password = sha256_str(input(Constant.ENTER_PASSWORD))

        while database.find(UserAccount, (UserAccount._UserAccount__username == username and
                                          UserAccount._UserAccount__password == password)):
            print(Constant.INCORRECT_LOGIN_PASSWORD)
            username = input(Constant.ENTER_USERNAME)
            password = sha256_str(input(Constant.ENTER_PASSWORD))

        user = database.get(UserAccount, (UserAccount._UserAccount__username == username and
                                          UserAccount._UserAccount__password == password))
        return user
