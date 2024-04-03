import os


class Constant:

    HI_TO_USER = "Привет, вы кто?"
    CHOOSE_STATUS = f" 1. Админ\n 2. Пользователь\n[1/2]?: "
    CHOOSE_OPTION = f"Выберите правильный вариант\n[0/1/2]?: " # CHOOSE_OPTION_1
    ENTER_SECRET_KEY = "Введите код доступа: "
    WRONG_KEY = "Неверный код доступа, введите еще раз: "
    CHOOSE_ACTIONS = f" 0. Назад\n 1. Зарегистрироваться\n 2. Войти в аккаунт\n[0/1/2]?: " # CHOOSE_OPTION_2
    CHOOSE_CORRECT_OPTION = f"Выберите правильный вариант\n[0/1/2]?: "
    ENTER_NAME = "Введите ваше имя: "
    ENTER_SURNAME = "Введите вашу Фамилию: "
    ENTER_BIRTH_DATE = "Введите дату вашего рождения: "
    ENTER_YOUR_SEX = "Пол [M/Ж]: "
    ENTER_PASSPORT_ID = f"Номер вашего паспорта: "
    ENTER_USERNAME = "Введите логин: "
    ENTER_PHONE_NUMBER = f"Введите ваш номер: "
    ENTER_PASSWORD = "Введите пароль: "
    INCORRECT_LOGIN_PASSWORD = "Вы ввели неправильный пароль или логин, попробуйте еще раз"
    SELECT_OPTION = "Выбери что вы хотите сделать\n 0. Выйти\n 1. Создать Тариф\n 2. Поменять Тариф\n 3. Список Тарифов\n[0/1/2/3]?:" # CHOOSE_OPTION_3
    ENTER_COST_GB_TARIFF = "Задайте цену одного гигибайта: "
    ENTER_COST_MINUTE_TARIFF = "Задайте цену одного мегабайта: "
    ENTER_GB_TARIFF = "Объем гигайбайтов в тарифе: "
    ENTER_MINUTE_TARIFF = "Объем минут в тарифе: "
    ENTER_PRICE_TARIFF = "Задайте цену тарифа: "
    LIST_SERVICES = "Список услуг:"
    SELECT_SERVICE = "Выберите номер услуги: " # CHOOSE_OPTION_4
    CHOOSE_CORRECT_OPTION_OF_SERVICES = "Выберите правильную опцию(номер услуги из предлогаемых): " # CHOOSE_CORRECT_OPTION_2
    ENTER_NEW_COST_GB_TARIFF = "Задайте новую цену одного гигибайта: "
    ENTER_NEW_COST_MINUTE_TARIFF = "Задайте новую цену одного мегабайта: "
    ENTER_NEW_GB_TARIFF = "Новый объем гигайбайтов в тарифе: "
    ENTER_NEW_MINUTE_TARIFF = "Новый объем минут в тарифе: "
    ENTER_NEW_PRICE_TARIFF = "Задайте новую цену тарифа: "
    SELECT_OPTION_OF_USER = (f"Выберите что вы хотите сделать\n 0. Выйти \n 1. Мой профиль\n 2. Поделится гигабайтами\n"
                       f" 3. Поделится минутами\n 4. Пополнить баланс\n 5. Поменять тариф\n"
                       f" 6. Купить гигабайты\n 7. Купить минуты\n 8. Оплатить тариф \n[0, 1,...,8]?: ") # CHOOSE_OPTION_5
    ENTER_FRIEND_PHONE_NUMBER = "Введите номер получателя: "
    ENTER_SEND_GB_ = "Введите сколько гигабайт хотите отправить: "
    ENTER_SEND_MINUTE = "Введите сколько минут хотите отправить: "
    ENTER_AMOUNT = "Введите сумму: "
    ENTER_CORRECT_AMOUNT = "Введите корректную сумму: "
    SELECT_TARIFF = "Выберите нужный тариф из списка: " # CHOOSE_OPTION_6
    ENTER_VALUE_GB = "Сколько гб хотите приобрести по стоимости:"
    ENTER_CORRECT_VALUE = "Введите корректное число: "
    ENTER_VALUE_MINUTE = "Сколько минут хотите приобрести по стоимости:"
    SUCCESSFUL_NEW_TARIFF = "Тариф успешно создан!"
    SUCCESSFUL_UPDATE_TARIFF = "Тариф успешно обновлен!"

class AdminConstants:

class UserConstants:

class TariffConstants:

class AuthorizationConstants:
