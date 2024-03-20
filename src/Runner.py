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
        variant = int(input(Constant.CHOOSE_STATUS))
        while True:
            if int(variant) not in [1, 2]:
                variant = int(input(Constant.CHOOSE_OPTION_1))
                continue
            break

        if variant == 1:
            key = input(Constant.ENTER_SECRET_KEY)
            while sha256_str(key) != Constant.SECRET_KEY:
                key = input(Constant.WRONG_KEY)

            variant = int(input(Constant.CHOOSE_OPTION_2))
            while True:
                if int(variant) not in [1, 2]:
                    variant = int(input(Constant.CHOOSE_CORRECT_OPTION))
                    continue
                break

            if variant == 1:

                first_name = input(Constant.ENTER_NAME)
                last_name = input(Constant.ENTER_SURNAME)
                birth_date = input(Constant.ENTER_BIRTH_DATE)
                sex = input(Constant.ENTER_YOUR_SEX)
                passport_id = int(input(Constant.ENTER_PASSPORT_ID))
                phone_number = input(Constant.ENTER_PHONE_NUMBER)
                username = input(Constant.ENTER_USERNAME)
                password = input(Constant.ENTER_PASSWORD)

                Admin = AdminAccount(first_name, last_name, birth_date, passport_id, sex,
                                     username, password, phone_number)

                s.add(Admin)
                s.commit()

            else:

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

                Admin = result[0]

            while True:

                variant = int(input(Constant.CHOOSE_OPTION_3))
                while True:
                    if variant not in [1, 2, 3]:
                        variant = int(input(Constant.CHOOSE_OPTION_3))
                        continue
                    break

                if variant == 1:

                    cost_one_gb = int(input(Constant.ENTER_COST_GB_TARIFF))
                    cost_one_minute = int(input(Constant.ENTER_COST_MINUTE_TARIFF))
                    gb = int(input(Constant.ENTER_GB_TARIFF))
                    minute = int(input(Constant.ENTER_MINUTE_TARIFF))
                    price = int(input(Constant.ENTER_PRICE_TARIFF))

                    new_tariff = Admin.create_tariff(cost_one_gb,
                                                     cost_one_minute, gb, minute, price)

                    s.add(new_tariff)
                    s.commit()

                elif variant == 2:
                    list_of_tariff = s.query(Tariff)

                    print(Constant.LIST_SERVICES)
                    for elem in list_of_tariff:
                        print(
                            f"{elem.id}: {elem.get_gb()}ГБ. | {elem.get_minutes()}мин. |"
                            f" {elem.get_cost_one_gb()}руб/гб. "
                            f"| {elem.get_cost_one_minute()}руб/гб. | {elem.get_price()}руб.")
                    option = int(input(Constant.CHOOSE_OPTION_4))

                    while not (
                            (list_of_tariff[0]).id <= option <= (list_of_tariff[list_of_tariff.count() - 1]).id):
                        option = int(input(Constant.CHOOSE_CORRECT_OPTION_2))

                    cost_one_gb = int(input(Constant.ENTER_NEW_COST_GB_TARIFF))
                    cost_one_minute = int(input(Constant.ENTER_NEW_COST_MINUTE_TARIFF))
                    gb = int(input(Constant.ENTER_NEW_GB_TARIFF))
                    minute = int(input(Constant.ENTER_NEW_MINUTE_TARIFF))
                    price = int(input(Constant.ENTER_NEW_PRICE_TARIFF))

                    tariff = s.query(Tariff).filter(Tariff.id == option).all()[0];
                    Admin.change_tariff(tariff, cost_one_gb, cost_one_minute, price, gb, minute)

                    s.add(tariff)
                    s.commit()

                else:
                    list_of_tariff = s.query(Tariff)

                    print(Constant.LIST_SERVICES)
                    for elem in list_of_tariff:
                        print(
                            f"{elem.id}: {elem.get_gb()}ГБ. | {elem.get_minutes()}мин. |"
                            f" {elem.get_cost_one_gb()}руб/гб. "
                            f"| {elem.get_cost_one_minute()}руб/гб. | {elem.get_price()}руб.")

        else:
            variant = int(input(Constant.CHOOSE_OPTION_2))
            while True:
                if int(variant) not in [1, 2]:
                    variant = int(input(Constant.CHOOSE_OPTION_1))
                    continue
                break

            if variant == 1:

                first_name = input(Constant.ENTER_NAME)
                last_name = input(Constant.ENTER_SURNAME)
                birth_date = input(Constant.ENTER_BIRTH_DATE)
                sex = input(Constant.ENTER_YOUR_SEX)
                passport_id = int(input(Constant.ENTER_PASSPORT_ID))
                phone_number = input(Constant.ENTER_PHONE_NUMBER)
                username = input(Constant.ENTER_USERNAME)
                password = input(Constant.ENTER_PASSWORD)

                list_of_tariff = s.query(Tariff)
                print(Constant.LIST_SERVICES)
                for elem in list_of_tariff:
                    print(f"{elem.id}: {elem.get_gb()}ГБ. | {elem.get_minutes()}мин. |"
                          f" {elem.get_cost_one_gb()}руб/гб. "
                          f"| {elem.get_cost_one_minute()}руб/гб. | {elem.get_price()}руб.")

                option = int(input(Constant.CHOOSE_OPTION_4))
                while not (
                        (list_of_tariff[0]).id <= option <= (list_of_tariff[list_of_tariff.count() - 1]).id):
                    option = int(input(Constant.CHOOSE_CORRECT_OPTION_2))

                User = UserAccount(first_name, last_name, birth_date, passport_id, sex,
                                   username, sha256_str(password), phone_number,
                                   (s.query(Tariff).filter(Tariff.id == option).all())[0])

                s.add(User)
                s.commit()

            else:
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
                        UserAccount._UserAccount__username == username
                        and UserAccount._UserAccount__password == password).all()

                User = result[0]

            while True:
                while (variant := int(
                        input(Constant.CHOOSE_OPTION_5))) not in [1, 2, 3, 4, 5, 6,7, 8]:
                    continue
                match variant:
                    case 1:

                        print(type(User))
                        print(f"Остаток: {User.get_gb()}ГБ. | {User.get_minutes()}мин. | {User.get_balance()}руб.\n"
                              f"Ваш Тариф: {User.get_tariff().get_gb()} ГБ | {User.get_tariff().get_minutes()}мин. |"
                              f" {User.get_tariff().get_cost_one_gb()}руб/гб. | {User.get_tariff().get_cost_one_minute()}руб/мин.")

                    case 2:

                        phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
                        owner_of_number = s.query(UserAccount).filter(
                            UserAccount._UserAccount__phone_number == phone_number).all()
                        while len(owner_of_number) == 0:
                            phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
                            owner_of_number = s.query(UserAccount).filter(
                                UserAccount._UserAccount__phone_number == phone_number).all()
                        how_many_gb = int(input(Constant.ENTER_SEND_GB_))
                        print(User.share_gb(owner_of_number[0], how_many_gb))

                        s.add(owner_of_number[0])
                        s.commit()

                    case 3:

                        phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
                        owner_of_number = s.query(UserAccount).filter(
                            UserAccount._UserAccount__phone_number == phone_number).all()
                        while len(owner_of_number) == 0:
                            phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
                            owner_of_number = s.query(UserAccount).filter(
                                UserAccount._UserAccount__phone_number == phone_number).all()

                        how_many_minute = int(input(Constant.ENTER_SEND_MINUTE))
                        User.share_minute(owner_of_number[0], how_many_minute)

                        s.add(owner_of_number[0])
                        s.commit()

                    case 4:

                        sum = int(input(Constant.ENTER_AMOUNT))
                        while True:
                            if not 0 < sum < 10000:
                                sum = int(input(Constant.ENTER_CORRECT_AMOUNT))
                                continue
                            break

                        User.deposit(sum)

                        s.add(User)
                        s.commit()

                    case 5:

                        list_of_tariff = s.query(Tariff)
                        print(Constant.LIST_SERVICES)
                        for elem in list_of_tariff:
                            print(
                                f"{elem.id}: {elem.get_gb()}ГБ. | {elem.get_minutes()}мин. |"
                                f" {elem.get_cost_one_gb()}руб/гб. "
                                f"| {elem.get_cost_one_minute()}руб/гб. | {elem.get_price()}руб.")

                        id = int(input(Constant.CHOOSE_OPTION_6))
                        tariff = s.query(Tariff).filter(Tariff.id == id).all()[0]
                        User.set_tariff(tariff)

                        s.add(User)
                        s.commit()

                    case 6:

                        value = int(input(
                            f"{Constant.ENTER_VALUE_GB}"
                            f" {User.get_tariff().get_cost_one_gb()}руб/гб.?: "))
                        while value <= 0:
                            value = int(input(Constant.ENTER_CORRECT_VALUE))

                        print(User.buy_gb(value))

                        s.add(User)
                        s.commit()

                    case 7:

                        value = int(input(
                            f"{Constant.ENTER_VALUE_MINUTE}"
                            f" {User.get_tariff().get_cost_one_minute()}руб/мин.?: "))
                        while value <= 0:
                            value = int(input(Constant.ENTER_CORRECT_VALUE))

                        print(User.buy_minute(value))

                        s.add(User)
                        s.commit()

                    case 8:

                        print(User.pay_tariff())

                        s.add(User)
                        s.commit()


App.run()
