from AdminAccount import AdminAccount, Tariff
from Constants import Constant
from Runner import Authorization, database


class HandleAdmin(AdminAccount):
    def create_new_tariff(self):
        cost_one_gb = int(input(Constant.ENTER_COST_GB_TARIFF))
        cost_one_minute = int(input(Constant.ENTER_COST_MINUTE_TARIFF))
        gb = int(input(Constant.ENTER_GB_TARIFF))
        minute = int(input(Constant.ENTER_MINUTE_TARIFF))
        price = int(input(Constant.ENTER_PRICE_TARIFF))

        new_tariff = self.create_tariff(cost_one_gb, cost_one_minute, gb, minute, price)

        database.insert(new_tariff)

        print(Constant.SUCCESSFUL_NEW_TARIFF)

    def update_existing_tariff(self):
        list_of_tariff = database.query(Tariff)

        Authorization.view_tariffs()

        option = int(input(Constant.CHOOSE_OPTION_4))

        while not (
                list_of_tariff[0].id <= option <= list_of_tariff[list_of_tariff.count() - 1].id):
            option = int(input(Constant.CHOOSE_CORRECT_OPTION_2))

        cost_one_gb = int(input(Constant.ENTER_NEW_COST_GB_TARIFF))
        cost_one_minute = int(input(Constant.ENTER_NEW_COST_MINUTE_TARIFF))
        gb = int(input(Constant.ENTER_NEW_GB_TARIFF))
        minute = int(input(Constant.ENTER_NEW_MINUTE_TARIFF))
        price = int(input(Constant.ENTER_NEW_PRICE_TARIFF))

        tariff = database.get_object(Tariff, (Tariff.id == option))
        self.change_tariff(tariff, cost_one_gb, cost_one_minute, price, gb, minute)

        database.insert(self)

        print(Constant.SUCCESSFUL_UPDATE_TARIFF)

    def handle_admin_actions(self):
        while True:
            action = int(input(Constant.CHOOSE_OPTION_3))
            while action not in [0, 1, 2, 3]:
                action = int(input(Constant.CHOOSE_OPTION_3))

            if action == 0:
                return
            if action == 1:
                AdminAccount.create_new_tariff(self)
            elif action == 2:
                AdminAccount.update_existing_tariff(self)
            elif action == 3:
                Authorization.view_tariffs()
