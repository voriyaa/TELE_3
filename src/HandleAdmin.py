# -*- coding: utf-8 -*-
from AdminAccount import AdminAccount, Tariff
from Constants import Constant
from Runner import database


class HandleAdmin(AdminAccount):

    @staticmethod
    def handle_admin_actions(admin):
        while True:
            action = int(input(Constant.SELECT_OPTION))
            while action not in [0, 1, 2, 3]:
                action = int(input(Constant.SELECT_OPTION))

            if action == 0:
                return
            if action == 1:
                HandleAdmin.create_new_tariff(admin)
            elif action == 2:
                HandleAdmin.update_existing_tariff(admin)
            elif action == 3:
                HandleAdmin.view_tariffs()

    @staticmethod
    def create_new_tariff(admin):
        cost_one_gb = int(input(Constant.ENTER_COST_GB_TARIFF))
        cost_one_minute = int(input(Constant.ENTER_COST_MINUTE_TARIFF))
        gb = int(input(Constant.ENTER_GB_TARIFF))
        minute = int(input(Constant.ENTER_MINUTE_TARIFF))
        price = int(input(Constant.ENTER_PRICE_TARIFF))

        new_tariff = admin.create_tariff(cost_one_gb, cost_one_minute, gb, minute, price)

        database.insert(new_tariff)

        print(Constant.SUCCESSFUL_NEW_TARIFF)

    @staticmethod
    def update_existing_tariff(admin):
        list_of_tariff = database.query(Tariff)

        HandleAdmin.view_tariffs()

        option = int(input(Constant.SELECT_SERVICE))

        while not (list_of_tariff[0].id <= option <= list_of_tariff[list_of_tariff.count() - 1].id):
            option = int(input(Constant.CHOOSE_CORRECT_OPTION_OF_SERVICES))

        cost_one_gb = int(input(Constant.ENTER_NEW_COST_GB_TARIFF))
        cost_one_minute = int(input(Constant.ENTER_NEW_COST_MINUTE_TARIFF))
        gb = int(input(Constant.ENTER_NEW_GB_TARIFF))
        minute = int(input(Constant.ENTER_NEW_MINUTE_TARIFF))
        price = int(input(Constant.ENTER_NEW_PRICE_TARIFF))

        tariff = database.get_object(Tariff, (Tariff.id == option))
        admin.change_tariff(tariff, cost_one_gb, cost_one_minute, price, gb, minute)

        database.insert(admin)

        print(Constant.SUCCESSFUL_UPDATE_TARIFF)

    @staticmethod
    def view_tariffs():
        list_of_tariff = database.query(Tariff)

        print(Constant.LIST_SERVICES)
        for elem in list_of_tariff:
            print(
                f"{elem.id}: {elem.get_gb()}ГБ. | {elem.get_minutes()}мин. |"
                f" {elem.get_cost_one_gb()}руб/гб. "
                f"| {elem.get_cost_one_minute()}руб/гб. | {elem.get_price()}руб.")
