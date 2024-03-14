from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from hashlib import sha256
from BaseUser import Base
from AdminAccount import AdminAccount, Tariff
from UserAccount import UserAccount


def sha256_str(item):
    return sha256(str(item).encode()).hexdigest()


DATABASE_URL = "postgresql://postgres:123@192.168.0.105/test"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
s = session()


class App:

    @staticmethod
    def run():
        print(f"Привет, вы кто?:\n")
        variant = int(input(f"1. Админ\n 2. Пользователь\n [1/2]?: "))
        while True:
            if int(variant) not in [1, 2]:
                variant = int(input(f"Выберите правильный вариант\n [1/2]?: "))
                continue
            break

        if variant == 1:

            key = input(f"Введите код доступа: ")
            while key != '12345':
                key = input("Неверный код доступа, введите еще раз: ")

            variant = int(input(f"1. Зарегистрироваться\n 2. Войти в аккаунт\n [1/2]?: "))
            while True:
                if int(variant) not in [1, 2]:
                    variant = int(input(f"Выберите правильный вариант\n [1/2]?: "))
                    continue
                break

            if variant == 1:
                first_name = input(f"Введите ваше Имя: ")
                last_name = input(f"Введите вашу Фамилию: ")
                birth_date = input(f"Ведите дату вашего рождения: ")
                sex = input(f"Пол [M/Ж]: ")
                passport_id = int(input(f"Номер вашего паспорта: "))
                username = input(f"Введите логин: ")
                phone_number = input(f"Введите ваш номер: ")
                password = input(f"Введите пароль: ")

                Admin = AdminAccount(first_name, last_name, birth_date, passport_id, sex,
                                     username, password, phone_number)
                print("voris")
                s.add(Admin)
                s.commit()
            else:
                username = input(f"Введите логин: ")
                password = sha256_str(input(f"Введите пароль: "))
                result = s.query(AdminAccount).filter(
                    AdminAccount._AdminAccount__username == username and AdminAccount._AdminAccount__password == password).all()
                while len(result) == 0:
                    print("Вы ввели неправильный пароль или логин, попробуйте еще раз\n")
                    username = input(f"Введите логин: ")
                    password = sha256_str(input(f"Введите пароль: "))
                    result = s.query(AdminAccount).filter(
                        AdminAccount._AdminAccount__username == username and AdminAccount._AdminAccount__password == password).all()
                Admin = result[0]
            while True:
                variant = int(
                    input("Выбери что вы хотите сделать\n 1. Создать Тариф\n 2. Поменять Тариф\n [1/2]?:"))
                while True:
                    if variant not in [1, 2]:
                        variant = int(
                            input("Выбери правильный вариант\n 1. Создать Тариф\n 2. Поменять Тариф\n [1/2]?:"))
                        continue
                    break
                if variant == 1:
                    cost_one_gb = int(input("Задайте цену одного гигибайта: "))
                    cost_one_minute = int(input("Задайте цену одного мегабайта: "))
                    gb = int(input("Объем гигайбайтов в тарифе: "))
                    minute = int(input("Объем минут в тарифе: "))
                    price = int(input("Задайте цену тарифа: "))
                    print(type(Admin))
                    new_tariff = Admin.create_tariff(cost_one_gb, cost_one_minute, gb, minute, price)
                    s.add(new_tariff)
                    s.commit()
                else:
                    print("Эта функция еще недоступна")
        else:
            variant = int(input(f"1. Зарегистрироваться\n 2. Войти в аккаунт\n [1/2]?: "))
            while True:
                if int(variant) not in [1, 2]:
                    variant = int(input(f"Выберите правильный вариант\n [1/2]?: "))
                    continue
                break

            if variant == 1:
                first_name = input(f"Введите ваше Имя: ")
                last_name = input(f"Введите вашу Фамилию: ")
                birth_date = input(f"Ведите дату вашего рождения: ")
                sex = input(f"Пол [M/Ж]: ")
                passport_id = int(input(f"Номер вашего паспорта: "))
                username = input(f"Введите логин: ")
                phone_number = input(f"Введите ваш номер: ")
                password = input(f"Введите пароль: ")
                list_of_tariff = s.query(Tariff)
                print(f"Список услуг:")
                for elem in list_of_tariff:
                    print(f"{elem.id}: {elem.get_gb()}ГБ. | {elem.get_minutes()}мин. | {elem.get_cost_one_gb()}руб/гб. "
                          f"| {elem.get_cost_one_minute()}руб/гб. | {elem.get_price()}руб.")
                option = int(input("Выберите опцию(номер услуги): "))
                while not (list_of_tariff[0]).id <= option <= (list_of_tariff[list_of_tariff.count() - 1]).id:
                    option = int(input("Выберите правильную опцию(номер услуги из предлогаемых): "))

                User = UserAccount(first_name, last_name, birth_date, passport_id, sex,
                                   username, sha256_str(password), phone_number,
                                   (s.query(Tariff).filter(Tariff.id == option).all())[0])

                s.add(User)
                s.commit()
            else:
                username = input(f"Введите логин: ")
                password = sha256_str(input(f"Введите пароль: "))
                result = s.query(UserAccount).filter(
                    UserAccount._UserAccount__username == username and UserAccount._UserAccount__password == password).all()
                while len(result) == 0:
                    print("Вы ввели неправильный пароль или логин, попробуйте еще раз\n")
                    username = input(f"Введите логин: ")
                    password = sha256_str(input(f"Введите пароль: "))
                    result = s.query(UserAccount).filter_by(
                        UserAccount._UserAccount__username == username and UserAccount._UserAccount__password == password).all()
                User = result[0]
            while True:
                while (variant := int(
                        input(f"Выберите что вы хотите сделать\n 1. Мой профиль \n 2. Поделится гигабайтами \n"
                              f" 3. Поделится минутами \n 4. Пополнить баланс \n 5. Поменять тариф \n"
                              f" 6. Купить гигабайты \n 7. Купить минуты\n [1,...,8]?: "))) not in [1, 2, 3, 4, 5, 6,
                                                                                                   7, 8]:
                    continue
                match variant:
                    case 1:
                        print(type(User))
                        print(f"Остаток: {User.get_gb()}ГБ. | {User.get_minutes()}мин. | {User.get_balance()}руб.\n"
                              f"Ваш Тариф: {User.get_tariff().get_gb()} ГБ | {User.get_tariff().get_minutes()}мин. |"
                              f" {User.get_tariff().get_cost_one_gb()}руб/гб. | {User.get_tariff().get_cost_one_minute()}руб/мин.")
                    case 2:
                        phone_number = input("Введите номер получателя: ")
                        owner_of_number = s.query(UserAccount).filter_by(
                            UserAccount._UserAccount__phone_number == phone_number).all()
                        if len(owner_of_number) == 0:
                            phone_number = input("Введите номер получателя: ")
                            owner_of_number = s.query(UserAccount).filter_by(
                                UserAccount._UserAccount__phone_number == phone_number).all()
                        how_many_gb = int(input("Введите сколько гигабайт хотите отправить: "))
                        User.share_gb(owner_of_number[0], how_many_gb)
                        s.add(owner_of_number)
                        s.add(result)
                        s.commit()
                    case 3:
                        phone_number = input("Введите номер получателя: ")
                        owner_of_number = s.query(UserAccount).filter_by(
                            UserAccount._UserAccount__phone_number == phone_number).all()
                        if len(owner_of_number) == 0:
                            phone_number = input("Введите номер получателя: ")
                            owner_of_number = s.query(UserAccount).filter_by(
                                UserAccount._UserAccount__phone_number == phone_number).all()
                        how_many_gb = int(input("Введите сколько гигабайт хотите отправить: "))
                        User.share_minute(owner_of_number[0], how_many_gb)
                        s.add(owner_of_number)
                        s.add(result)
                        s.commit()
                    case 4:
                        sum = int(input(f"Введите сумму: "))
                        while True:
                            if not 0 < sum < 10000:
                                sum = int(input("Введите корректную сумму: "))
                                continue
                            break
                        User.deposit(sum)
                        s.add(result)
                        s.commit()


App.run()
