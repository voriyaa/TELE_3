from UserAccount import UserAccount
from Constants import Constant
from Runner import App
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
                    App.user_workflow()
                    break
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
        print(f"Остаток: {self.get_gb()}ГБ. | {self.get_minutes()}мин. | {self.get_balance()}руб.\n"
              f"Ваш Тариф: {self.get_tariff().get_gb()} ГБ | {self.get_tariff().get_minutes()}мин. |"
              f" {self.get_tariff().get_cost_one_gb()}руб/гб. | {self.get_tariff().get_cost_one_minute()}руб/мин.")

    def share_gb_with_friend(self):
        phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
        owner_of_number = s.query(UserAccount).filter(
            UserAccount._UserAccount__phone_number == phone_number).all()
        while len(owner_of_number) == 0:
            phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
            owner_of_number = s.query(UserAccount).filter(
                UserAccount._UserAccount__phone_number == phone_number).all()
        how_many_gb = int(input(Constant.ENTER_SEND_GB_))
        print(self.share_gb(owner_of_number[0], how_many_gb))
        s.add(owner_of_number[0])
        s.commit()

    def share_minute_with_friend(self):
        phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
        owner_of_number = s.query(UserAccount).filter(
            UserAccount._UserAccount__phone_number == phone_number).all()
        while len(owner_of_number) == 0:
            phone_number = input(Constant.ENTER_FRIEND_PHONE_NUMBER)
            owner_of_number = s.query(UserAccount).filter(
                UserAccount._UserAccount__phone_number == phone_number).all()

        how_many_minute = int(input(Constant.ENTER_SEND_MINUTE))
        self.share_minute(owner_of_number[0], how_many_minute)

        s.add(owner_of_number[0])
        s.commit()

    def deposit_money(self):
        amount = int(input(Constant.ENTER_AMOUNT))
        while not (0 < amount < 10000):
            amount = int(input(Constant.ENTER_CORRECT_AMOUNT))
        self.deposit(amount)
        s.add(self)
        s.commit()

    def change_tariff(self):
        list_of_tariff = s.query(Tariff)
        App.display_tariffs(list_of_tariff)
        id = int(input(Constant.CHOOSE_OPTION_6))
        tariff = s.query(Tariff).filter(Tariff.id == id).all()[0]
        self.set_tariff(tariff)
        s.add(self)
        s.commit()

    def handle_buy_gb(self):
        value = int(input(f"{Constant.ENTER_VALUE_GB}"
                          f" {self.get_tariff().get_cost_one_gb()}руб/гб.?: "))
        while value <= 0:
            value = int(input(Constant.ENTER_CORRECT_VALUE))
        print(self.buy_gb(value))
        s.add(self)
        s.commit()

    def handle_buy_minute(self):
        value = int(input(f"{Constant.ENTER_VALUE_MINUTE}"
                          f" {self.get_tariff().get_cost_one_minute()}руб/мин.?: "))
        while value <= 0:
            value = int(input(Constant.ENTER_CORRECT_VALUE))
        print(self.buy_minute(value))
        s.add(self)
        s.commit()

    def pay_tariff(self):
        print(self.pay_tariff())
        s.add(self)
        s.commit()