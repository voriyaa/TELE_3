from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2
import UserAccount
from hashlib import sha256
from BaseUser import Base
from AdminAccount import AdminAccount
from Tariff import Tariff
from UserAccount import  UserAccount


def sha256_str(item):
    return sha256(str(item).encode()).hexdigest()


DATABASE_URL = "postgresql://postgres:123@192.168.0.105/test"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


class App:

    @staticmethod
    def run(self):
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

            variant = input(f"1. Зарегистрироваться\n 2. Войти в аккаунт\n [1/2]?: ")
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
                                     username, sha256_str(password), phone_number)
                session.add(Admin)
                session.commit()
            else:
                username = input(f"Введите логин: ")
                password = sha256(input(f"Введите пароль: "))
                result = session.query(AdminAccount).filter_by(
                    AdminAccount._AdminAccount__username == username and AdminAccount._AdminAccount__password == password).all()
                while len(result) == 0:
                    print("Вы ввели неправильный пароль или логин, попробуйте еще раз\n")
                    username = input(f"Введите логин: ")
                    password = sha256(input(f"Введите пароль: "))
                    result = session.query(AdminAccount).filter_by(
                        AdminAccount._AdminAccount__username == username and AdminAccount._AdminAccount__password == password).all()
                Admin = result[0]
            while True:
                variant = int(
                    input("Выбери что вы хотите сделать\n 1. Создать Тариф\n 2. Поменять Тариф\n [1/2]?:"))
                while True:
                    if variant not in [1, 2]:
                        variant = int(input("Выбери правильный вариант\n 1. Создать Тариф\n 2. Поменять Тариф\n [1/2]?:"))
                        continue
                    break
                if variant == 1:
                    cost_one_gb = int(input("Задайте цену одного гигибайта: "))
                    cost_one_minute = int(input("Задайте цену одного мегабайта: "))
                    gb = int(input("Объем гигайбайтов в тарифе: "))
                    minute = int(input("Объем минут в тарифе: "))
                    price = int(input("Задайте цену тарифа: "))
                    new_tariff = Admin.creat_tariff(cost_one_gb, cost_one_minute, gb, minute, price)
                    #database
                else:
                    print("Эта функция еще недоступна")
        else:
            variant = input(f"1. Зарегистрироваться\n 2. Войти в аккаунт\n [1/2]?: ")
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
                #database
                User = UserAccount(first_name, last_name, birth_date, passport_id, sex,
                                   username, sha256_str(password), phone_number, '''main_tariff''')
            else:
                username = input(f"Введите логин: ")
                password = sha256(input(f"Введите пароль: "))
                result = session.query(UserAccount).filter_by(
                    UserAccount._UserAccount__username == username and UserAccount._UserAccount__password == password).all()
                while len(result) == 0:
                    print("Вы ввели неправильный пароль или логин, попробуйте еще раз\n")
                    username = input(f"Введите логин: ")
                    password = sha256(input(f"Введите пароль: "))
                    result = session.query(UserAccount).filter_by(
                        UserAccount._UserAccount__username == username and UserAccount._UserAccount__password == password).all()
                User = result[0]
                while True:
                    variant = int(
                        input(f"Выбери что вы хотите сделать\n 1. Мой профиль \n"))
                    while True:
                        if variant not in [1, 2]:
                            pass
                            continue
                        break

