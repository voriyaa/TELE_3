import os


class AdminConstants:
    SELECT_OPTION = ("Выберите что вы хотите сделать\n 0. Выйти\n 1. Создать Тариф\n 2. Поменять Тариф\n 3. Список "
                     "Тарифов\n[0/1/2/3]?:")  # CHOOSE_OPTION_3
    SELECT_VALID_OPTION = f"Выберите правильный вариант\n[0/1/2/3]?: "
    SUCCESSFUL_NEW_TARIFF = "Тариф успешно создан!"
    SELECT_SERVICE = "Выберите номер услуги: "  # CHOOSE_OPTION_4
    CHOOSE_VALID_OPTION_OF_SERVICES = "Выберите правильную опцию(номер услуги из предлогаемых): "  # CHOOSE_VALID_OPTION_2
    SUCCESSFUL_UPDATE_TARIFF = "Тариф успешно обновлен!"
    LIST_SERVICES = "Список услуг:"


class UserConstants:
    SELECT_OPTION_OF_USER = (f"Выберите что вы хотите сделать\n 0. Выйти \n 1. Мой профиль\n 2. Поделится гигабайтами\n"
                             f" 3. Поделится минутами\n 4. Пополнить баланс\n 5. Поменять тариф\n"
                             f" 6. Купить гигабайты\n 7. Купить минуты\n 8. Оплатить тариф \n[0,1,...,8]?: ")  # CHOOSE_OPTION_5
    SELECT_VALID_OPTION_OF_USER = "Выберите правильный вариант\n[0,1,...,8]?: "
    ENTER_FRIEND_PHONE_NUMBER = "Введите номер получателя: "
    ENTER_SEND_GB = "Введите сколько гигабайт хотите отправить: "
    ERROR = "Ошибка!"
    ENTER_SEND_MINUTE = "Введите сколько минут хотите отправить: "
    ENTER_AMOUNT = "Введите сумму: "
    ENTER_VALID_AMOUNT = "Введите корректную сумму: "
    SELECT_TARIFF = "Выберите нужный тариф из списка: "  # CHOOSE_OPTION_6
    CHOOSE_VALID_OPTION_OF_SERVICES = "Выберите правильную опцию(номер услуги из предлогаемых): "  # CHOOSE_VALID_OPTION_2
    ENTER_VALUE_GB = "Сколько гб хотите приобрести по стоимости:"
    ENTER_VALID_VALUE = "Введите корректное число: "
    ENTER_VALUE_MINUTE = "Сколько минут хотите приобрести по стоимости:"
    LIST_SERVICES = "Список услуг:"


class AuthorizationConstants:
    GREET_USER = "Привет, вы кто?"
    CHOOSE_STATUS = f" 1. Админ\n 2. Пользователь\n[1/2]?: "
    CHOOSE_OPTION = f"Выберите правильный вариант\n[1/2]?: "  # CHOOSE_OPTION_1
    CHOOSE_ACTIONS = f" 0. Назад\n 1. Зарегистрироваться\n 2. Войти в аккаунт\n[0/1/2]?: "  # CHOOSE_OPTION_2
    CHOOSE_VALID_OPTION = f"Выберите правильный вариант\n[0/1/2]?: "
    ENTER_SECRET_KEY = "Введите код доступа: "
    WRONG_KEY = "Неверный код доступа, введите еще раз: "
    INVALID_LOGIN_PASSWORD = "Вы ввели неправильный пароль или логин, попробуйте еще раз"
    LIST_SERVICES = "Список услуг:"
    SELECT_SERVICE = "Выберите номер услуги: "  # CHOOSE_OPTION_4
    CHOOSE_VALID_OPTION_OF_SERVICES = "Выберите правильную опцию(номер услуги из предлогаемых): "  # CHOOSE_VALID_OPTION_2


class GetInfoConstants:
    ENTER_NAME = "Введите ваше Имя: "
    ENTER_SURNAME = "Введите вашу Фамилию: "
    ENTER_BIRTH_DATE = "Введите дату вашего рождения: "
    ENTER_YOUR_SEX = "Пол [M/Ж]: "
    ENTER_PASSPORT_ID = f"Номер вашего паспорта: "
    ENTER_USERNAME = "Введите логин: "
    ENTER_PHONE_NUMBER = f"Введите ваш номер: "
    ENTER_PASSWORD = "Введите пароль: "
    ENTER_COST_GB_TARIFF = "Задайте цену одного гигибайта: "
    ENTER_COST_MINUTE_TARIFF = "Задайте цену одного мегабайта: "
    ENTER_GB_TARIFF = "Объем гигайбайтов в тарифе: "
    ENTER_MINUTE_TARIFF = "Объем минут в тарифе: "
    ENTER_PRICE_TARIFF = "Задайте цену тарифа: "
