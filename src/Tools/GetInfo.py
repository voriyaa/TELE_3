from src.Constants.Constants import GetInfoConstants
from hashlib import sha256


def sha256_str(item):
    return sha256(str(item).encode()).hexdigest()


class GetInfo:

    @staticmethod
    def preregistration() -> dict:
        info = dict()

        info['first_name'] = input(GetInfoConstants.ENTER_NAME)
        info['last_name'] = input(GetInfoConstants.ENTER_SURNAME)
        info['birth_date'] = input(GetInfoConstants.ENTER_BIRTH_DATE)
        info['sex'] = input(GetInfoConstants.ENTER_YOUR_SEX)
        info['passport_id'] = input(GetInfoConstants.ENTER_PASSPORT_ID)
        info['phone_number'] = input(GetInfoConstants.ENTER_PHONE_NUMBER)
        info['username'] = input(GetInfoConstants.ENTER_USERNAME)
        info['password'] = sha256_str(input(GetInfoConstants.ENTER_PASSWORD))

        return info

    @staticmethod
    def info_account() -> dict:
        info = dict()

        info['username'] = input(GetInfoConstants.ENTER_USERNAME)
        info['password'] = sha256_str(input(GetInfoConstants.ENTER_PASSWORD))

        return info

    @staticmethod
    def info_tariff() -> dict:
        info = dict()

        info['cost_one_gb'] = int(input(GetInfoConstants.ENTER_COST_GB_TARIFF))
        info['cost_one_minute'] = int(input(GetInfoConstants.ENTER_COST_MINUTE_TARIFF))
        info['gb'] = int(input(GetInfoConstants.ENTER_GB_TARIFF))
        info['minute'] = int(input(GetInfoConstants.ENTER_MINUTE_TARIFF))
        info['price'] = int(input(GetInfoConstants.ENTER_PRICE_TARIFF))

        return info
