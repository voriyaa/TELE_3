from UserAccount import UserAccount
from Constants import Constant
from Runner import database
from AdminAccount import Tariff


class HandleUser(UserAccount):

    def handle_user_actions(self):
        while True:
            variant = int(input(Constant.CHOOSE_OPTION_5))
            while variant not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                print(Constant.CHOOSE_CORRECT_OPTION)
                variant = int(input(Constant.CHOOSE_OPTION_5))

            match variant:
                case 0:
                    return
                case 1:
                    self.show_user_details()
                case 2:
                    self.share_gb_with_friend()
                case 3:
                    self.share_minute_with_friend()
                case 4:
                    self.deposit_money()
                case 5:
                    self.change_tariff()
                case 6:
                    self.handle_buy_gb()
                case 7:
                    self.handle_buy_minute()
                case 8:
                    self.pay_tariff()

    def show_user_details(self):
        print(f"�������: {self.get_gb()}��. | {self.get_minutes()}���. | {self.get_balance()}���.\n"
              f"��� �����: {self.get_tariff().get_gb()} �� | {self.get_tariff().get_minutes()}���. |"
              f" {self.get_tariff().get_cost_one_gb()}���/��. | {self.get_tariff().get_cost_one_minute()}���/���.")

    def share_gb_with_friend(self):
        phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
        while database.find(UserAccount, phone_number, UserAccount._UserAccount__phone_number == phone_number):
            phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
        owner_of_number = database.get_object(UserAccount, (
                UserAccount._UserAccount__phone_number == phone_number))
        how_many_gb = int(input(Constant.ENTER_SEND_GB_))
        print(self.share_gb(owner_of_number, how_many_gb))
        database.insert(owner_of_number)


    def share_minute_with_friend(self):
        phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
        while database.find(UserAccount, phone_number, UserAccount._UserAccount__phone_number == phone_number):
            phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
        owner_of_number = database.get_object(UserAccount, (
                UserAccount._UserAccount__phone_number == phone_number))
        how_many_minute = int(input(Constant.ENTER_SEND_MINUTE))
        self.share_minute(owner_of_number, how_many_minute)

        database.insert(owner_of_number)

    def deposit_money(self):
        amount = int(input(Constant.ENTER_AMOUNT))
        while not (0 < amount < 10000):
            amount = int(input(Constant.ENTER_CORRECT_AMOUNT))
        self.deposit(amount)
        database.insert(self)

    def change_tariff(self):
        list_of_tariff = database.query(Tariff)
        HandleUser.display_tariffs(list_of_tariff)
        id = int(input(Constant.CHOOSE_OPTION_6))
        tariff = database.get_object(Tariff, (Tariff.id == id))
        self.set_tariff(tariff)
        database.insert(self)

    def handle_buy_gb(self):
        value = int(input(f"{Constant.ENTER_VALUE_GB}"
                          f" {self.get_tariff().get_cost_one_gb()}���/��.?: "))
        while value <= 0:
            value = int(input(Constant.ENTER_CORRECT_VALUE))
        print(self.buy_gb(value))
        database.insert(self)

    def handle_buy_minute(self):
        value = int(input(f"{Constant.ENTER_VALUE_MINUTE}"
                          f" {self.get_tariff().get_cost_one_minute()}���/���.?: "))
        while value <= 0:
            value = int(input(Constant.ENTER_CORRECT_VALUE))
        print(self.buy_minute(value))
        database.insert(self)

    def pay_tariff(self):
        print(self.pay_tariff())
        database.insert(self)

    @staticmethod
    def display_tariffs(tariffs):
        print(Constant.LIST_SERVICES)
        for i, elem in enumerate(tariffs):
            print(
                f"{i + 1}: {elem.get_gb()}ГБ. | {elem.get_minutes()}мин. |"
                f" {elem.get_cost_one_gb()}руб/гб. "
                f"| {elem.get_cost_one_minute()}руб/гб. | {elem.get_price()}руб.")
