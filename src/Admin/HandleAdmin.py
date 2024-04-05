# -*- coding: utf-8 -*-
from src.Admin.AdminAccount import AdminAccount, Tariff
from src.Constants.Constants import AdminConstants
from src.Authorization.Authorization import database
from src.Tools.GetInfo import GetInfo
from src.Tools.GetCorrectValue import GetCorrectValue


class HandleAdmin(AdminAccount):

    @staticmethod
    def handle_admin_actions(admin):
        while True:
            variant = GetCorrectValue.get_number(min_value=0,
                                                 max_value=3,
                                                 first_out=AdminConstants.SELECT_OPTION,
                                                 second_out=AdminConstants.SELECT_VALID_OPTION)
            actions = {
                1: lambda: HandleAdmin.create_new_tariff(admin),
                2: lambda: HandleAdmin.update_existing_tariff(admin),
                3: lambda: HandleAdmin.view_tariffs()
            }
            if variant == 0:
                return None
            actions[variant]()

    @staticmethod
    def create_new_tariff(admin):
        info = GetInfo.info_tariff()

        new_tariff = admin.create_tariff(info['cost_one_gb'], info['cost_one_minute'],
                                         info['gb'], info['minute'], info['price'])

        database.insert(new_tariff)

        print(AdminConstants.SUCCESSFUL_NEW_TARIFF)

    @staticmethod
    def update_existing_tariff(admin):
        list_of_tariff = database.query(Tariff)

        HandleAdmin.view_tariffs()

        option = input(AdminConstants.SELECT_SERVICE)
        while not (
                option.isdigit() and
                list_of_tariff[0].id <= int(option) <= list_of_tariff[list_of_tariff.count() - 1].id
        ):
            option = input(AdminConstants.CHOOSE_VALID_OPTION_OF_SERVICES)
        option = int(option)

        info = GetInfo.info_tariff()

        tariff = database.get_object(Tariff, (Tariff.id == option, True))
        admin.change_tariff(tariff, info['gb'], info['minute'],
                            info['cost_one_gb'], info['cost_one_minute'], info['price'])

        database.insert(admin)

        print(AdminConstants.SUCCESSFUL_UPDATE_TARIFF)

    @staticmethod
    def view_tariffs():
        list_of_tariff = database.query(Tariff)

        print(AdminConstants.LIST_SERVICES)
        for elem in list_of_tariff:
            print(
                f"{elem.id}: {elem.get_gb()}ГБ. | {elem.get_minutes()}мин. |"
                f" {elem.get_cost_one_gb()}руб/гб. "
                f"| {elem.get_cost_one_minute()}руб/гб. | {elem.get_price()}руб.")
