# -*- coding: utf-8 -*-
from AdminAccount import AdminAccount, Tariff
from Constants import Constant
from Runner import database
from GetInfo import GetInfo
from GetCorrectValue import GetCorrectValue


class HandleAdmin(AdminAccount):

    @staticmethod
    def handle_admin_actions(admin):
        while True:
            action = GetCorrectValue.get_number(min_value=0,
                                                max_value=3,
                                                first_out=Constant.SELECT_OPTION,
                                                second_out=Constant.SELECT_CORRECT_OPTION)
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
        info = GetInfo.info_tariff()

        new_tariff = admin.create_tariff(info['cost_one_gb'], info['cost_one_minute'], info['gb'], info['minute'], info['price'])

        database.insert(new_tariff)

        print(Constant.SUCCESSFUL_NEW_TARIFF)

    @staticmethod
    def update_existing_tariff(admin):
        list_of_tariff = database.query(Tariff)

        HandleAdmin.view_tariffs()

        option = input(Constant.SELECT_SERVICE)
        while not (
                option.isdigit() and
                list_of_tariff[0].id <= int(option) <= list_of_tariff[list_of_tariff.count() - 1].id
        ):
            option = input(Constant.CHOOSE_CORRECT_OPTION_OF_SERVICES)
        option = int(option)

        info = GetInfo.info_tariff()

        tariff = database.get_object(Tariff, (Tariff.id == option))
        admin.change_tariff(tariff, info['gb'], info['minute'],
                            info['cost_one_gb'], info['cost_one_minute'], info['price'])

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
