class AdminAccount(BaseUser):

    def __init__(self, first_name, last_name, birth_date, passport_id, sex,
                 username: str, password: str, phone_number: str) -> None:
        super().__init__(first_name, last_name, birth_date, passport_id, sex)
        self.__username = username
        self.__password = password
        self.__phone_number = phone_number

    def create_tariff(self, cost_one_gb, cost_one_minute, price, gb, minute):
        pass

    @staticmethod
    def change_tariff(self, old_tariff: Tariff, cost_one_gb, cost_one_minute, price, gb, minute) -> None:
        old_tariff.change_tariff(cost_one_gb, cost_one_minute, price, gb, minute)
        pass
