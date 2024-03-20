from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from hashlib import sha256
from BaseUser import Base
from AdminAccount import AdminAccount, Tariff
from UserAccount import UserAccount
from Constants import Constant


def sha256_str(item):
    return sha256(str(item).encode()).hexdigest()


# DATABASE_URL = 'postgresql://postgres:123@192.168.0.105:5432/test'
db_file = 'example.db'

DATABASE_URL = f'sqlite:///{db_file}'

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)
s = session()


class App:

    @staticmethod
    def run():
        print(Constant.HI_TO_USER)
        variant = App.get_variant()

        if variant == 1:
            App.admin_workflow()
        else:
            App.user_workflow()

    @staticmethod
    def get_variant():
        variant = int(input(Constant.CHOOSE_STATUS))
        while variant not in [1, 2]:
            variant = int(input(Constant.CHOOSE_OPTION_1))
        return variant

    @staticmethod
    def create_new_tariff(admin):
        cost_one_gb = int(input(Constant.ENTER_COST_GB_TARIFF))
        cost_one_minute = int(input(Constant.ENTER_COST_MINUTE_TARIFF))
        gb = int(input(Constant.ENTER_GB_TARIFF))
        minute = int(input(Constant.ENTER_MINUTE_TARIFF))
        price = int(input(Constant.ENTER_PRICE_TARIFF))

        new_tariff = admin.create_tariff(cost_one_gb, cost_one_minute, gb, minute, price)

        s.add(new_tariff)
        s.commit()

        print(Constant.SUCCESSFUL_NEW_TARIFF)

    @staticmethod
    def update_existing_tariff(admin):
        list_of_tariff = s.query(Tariff)

        App.view_tariffs()

        option = int(input(Constant.CHOOSE_OPTION_4))

        while not (
                list_of_tariff[0].id <= option <= list_of_tariff[list_of_tariff.count() - 1].id):
            option = int(input(Constant.CHOOSE_CORRECT_OPTION_2))

        cost_one_gb = int(input(Constant.ENTER_NEW_COST_GB_TARIFF))
        cost_one_minute = int(input(Constant.ENTER_NEW_COST_MINUTE_TARIFF))
        gb = int(input(Constant.ENTER_NEW_GB_TARIFF))
        minute = int(input(Constant.ENTER_NEW_MINUTE_TARIFF))
        price = int(input(Constant.ENTER_NEW_PRICE_TARIFF))

        tariff = s.query(Tariff).filter(Tariff.id == option).all()[0]
        admin.change_tariff(tariff, cost_one_gb, cost_one_minute, price, gb, minute)

        s.add(tariff)
        s.commit()

        print(Constant.SUCCESSFUL_UPDATE_TARIFF)

    @staticmethod
    def view_tariffs():
        list_of_tariff = s.query(Tariff)

        print(Constant.LIST_SERVICES)
        for elem in list_of_tariff:
            print(
                f"{elem.id}: {elem.get_gb()}ГБ. | {elem.get_minutes()}мин. |"
                f" {elem.get_cost_one_gb()}руб/гб. "
                f"| {elem.get_cost_one_minute()}руб/гб. | {elem.get_price()}руб.")

    @staticmethod
    def admin_workflow():
        App.verify_secret_key()

        variant = App.choose_admin_option()
        if variant == 0:
            App.run()
            return
        elif variant == 1:
            admin = App.create_admin_account()
        else:
            admin = App.admin_login()

        App.handle_admin_action(admin)

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

        s.add(admin)
        s.commit()

        return admin

    @staticmethod
    def admin_login():
        username = input(Constant.ENTER_USERNAME)
        password = sha256_str(input(Constant.ENTER_PASSWORD))

        result = s.query(AdminAccount).filter(
            AdminAccount._AdminAccount__username == username and
            AdminAccount._AdminAccount__password == password).all()

        while len(result) == 0:
            print(Constant.INCORRECT_LOGIN_PASSWORD)
            username = input(Constant.ENTER_USERNAME)
            password = sha256_str(input(Constant.ENTER_PASSWORD))
            result = s.query(AdminAccount).filter(
                AdminAccount._AdminAccount__username == username and
                AdminAccount._AdminAccount__password == password).all()

        return result[0]

    @staticmethod
    def handle_admin_action(admin):
        while True:
            action = int(input(Constant.CHOOSE_OPTION_3))
            while action not in [0, 1, 2, 3]:
                action = int(input(Constant.CHOOSE_OPTION_3))

            if action == 0:
                break
            if action == 1:
                App.create_new_tariff(admin)
            elif action == 2:
                App.update_existing_tariff(admin)
            elif action == 3:
                App.view_tariffs()

        App.admin_workflow()

    @staticmethod
    def user_workflow():
        variant = App.choose_user_option()

        if variant == 0:
            App.run()
            return
        elif variant == 1:
            user = App.create_user_account()
        else:
            user = App.user_login()

        App.handle_user_actions(user)

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

        list_of_tariff = s.query(Tariff)
        App.display_tariffs(list_of_tariff)

        option = App.choose_tariff_option(list_of_tariff)

        user = UserAccount(first_name, last_name, birth_date, passport_id, sex,
                           username, password, phone_number,
                           list_of_tariff[option - 1])

        s.add(user)
        s.commit()

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

        result = s.query(UserAccount).filter(
            UserAccount._UserAccount__username == username and
            UserAccount._UserAccount__password == password).all()

        while len(result) == 0:
            print(Constant.INCORRECT_LOGIN_PASSWORD)
            username = input(Constant.ENTER_USERNAME)
            password = sha256_str(input(Constant.ENTER_PASSWORD))
            result = s.query(UserAccount).filter(
                UserAccount._UserAccount__username == username and
                UserAccount._UserAccount__password == password).all()

        user = result[0]
        return user

    @staticmethod
    def handle_user_actions(user):
        while True:
            variant = int(input(Constant.CHOOSE_OPTION_5))
            while variant not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                print(Constant.CHOOSE_CORRECT_OPTION)
                variant = int(input(Constant.CHOOSE_OPTION_5))

            match variant:
                case 0:
                    App.user_workflow()
                    break
                case 1:
                    App.show_user_details(user)
                case 2:
                    App.share_gb_with_friend(user)
                case 3:
                    App.share_minute_with_friend(user)
                case 4:
                    App.deposit_money(user)
                case 5:
                    App.change_tariff(user)
                case 6:
                    App.buy_gb(user)
                case 7:
                    App.buy_minute(user)
                case 8:
                    App.pay_tariff(user)

    @staticmethod
    def show_user_details(user):
        print(f"Остаток: {user.get_gb()}ГБ. | {user.get_minutes()}мин. | {user.get_balance()}руб.\n"
              f"Ваш Тариф: {user.get_tariff().get_gb()} ГБ | {user.get_tariff().get_minutes()}мин. |"
              f" {user.get_tariff().get_cost_one_gb()}руб/гб. | {user.get_tariff().get_cost_one_minute()}руб/мин.")

    @staticmethod
    def share_gb_with_friend(user):
        phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
        owner_of_number = s.query(UserAccount).filter(
            UserAccount._UserAccount__phone_number == phone_number).all()
        while len(owner_of_number) == 0:
            phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
            owner_of_number = s.query(UserAccount).filter(
                UserAccount._UserAccount__phone_number == phone_number).all()
        how_many_gb = int(input(Constant.ENTER_SEND_GB_))
        print(user.share_gb(owner_of_number[0], how_many_gb))
        s.add(owner_of_number[0])
        s.commit()

    @staticmethod
    def share_minute_with_friend(user):
        phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
        owner_of_number = s.query(UserAccount).filter(
            UserAccount._UserAccount__phone_number == phone_number).all()
        while len(owner_of_number) == 0:
            phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
            owner_of_number = s.query(UserAccount).filter(
                UserAccount._UserAccount__phone_number == phone_number).all()
        how_many_minute = int(input(Constant.ENTER_SEND_MINUTE))
        user.share_minute(owner_of_number[0], how_many_minute)
        s.add(owner_of_number[0])
        s.commit()

    @staticmethod
    def deposit_money(user):
        amount = int(input(Constant.ENTER_AMOUNT))
        while not (0 < amount < 10000):
            amount = int(input(Constant.ENTER_CORRECT_AMOUNT))
        user.deposit(amount)
        s.add(user)
        s.commit()

    @staticmethod
    def change_tariff(user):
        list_of_tariff = s.query(Tariff)
        App.display_tariffs(list_of_tariff)
        id = int(input(Constant.CHOOSE_OPTION_6))
        tariff = s.query(Tariff).filter(Tariff.id == id).all()[0]
        user.set_tariff(tariff)
        s.add(user)
        s.commit()

    @staticmethod
    def buy_gb(user):
        value = int(input(f"{Constant.ENTER_VALUE_GB}"
                          f" {user.get_tariff().get_cost_one_gb()}руб/гб.?: "))
        while value <= 0:
            value = int(input(Constant.ENTER_CORRECT_VALUE))
        print(user.buy_gb(value))
        s.add(user)
        s.commit()

    @staticmethod
    def buy_minute(user):
        value = int(input(f"{Constant.ENTER_VALUE_MINUTE}"
                          f" {user.get_tariff().get_cost_one_minute()}руб/мин.?: "))
        while value <= 0:
            value = int(input(Constant.ENTER_CORRECT_VALUE))
        print(user.buy_minute(value))
        s.add(user)
        s.commit()

    @staticmethod
    def pay_tariff(user):
        print(user.pay_tariff())
        s.add(user)
        s.commit()

App.run()
