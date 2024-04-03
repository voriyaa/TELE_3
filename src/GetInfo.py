from Constants import Constant
from hashlib import sha256


def sha256_str(item):
    return sha256(str(item).encode()).hexdigest()


class GetInfo:

    @staticmethod
    def preregistration() -> dict:
        info = dict()

        info['first_name'] = input(Constant.ENTER_NAME)
        info['last_name'] = input(Constant.ENTER_SURNAME)
        info['birth_date'] = input(Constant.ENTER_BIRTH_DATE)
        info['sex'] = input(Constant.ENTER_YOUR_SEX)
        info['passport_id'] = input(Constant.ENTER_PASSPORT_ID)
        info['phone_number'] = input(Constant.ENTER_PHONE_NUMBER)
        info['username'] = input(Constant.ENTER_USERNAME)
        info['password'] = input(Constant.ENTER_PASSWORD)

        return info

    @staticmethod
    def info_account() -> dict:
        info = dict()

        info['username'] = input(Constant.ENTER_USERNAME)
        info['password'] = sha256_str(input(Constant.ENTER_PASSWORD))

        return info

    @staticmethod
    def info_tariff() -> dict:
        info = dict()

        info['cost_one_gb'] = int(input(Constant.ENTER_COST_GB_TARIFF))
        info['cost_one_minute'] = int(input(Constant.ENTER_COST_MINUTE_TARIFF))
        info['gb'] = int(input(Constant.ENTER_GB_TARIFF))
        info['minute'] = int(input(Constant.ENTER_MINUTE_TARIFF))
        info['price'] = int(input(Constant.ENTER_PRICE_TARIFF))

        return info
