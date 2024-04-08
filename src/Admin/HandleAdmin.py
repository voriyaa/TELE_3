# -*- coding: utf-8 -*-
from src.Admin.AdminAccount import AdminAccount, Tariff
from src.Constants.Constants import AdminConstants
from src.Authorization.Authorization import database
from src.Tools.GetInfo import GetInfo
from flask_jwt_extended import create_access_token
from datetime import timedelta
from src.Tools.MyHashFunc import sha256


class HandleAdmin(AdminAccount):
    @staticmethod
    def create_admin_account(**kwargs):
        admin = AdminAccount(**kwargs)
        database.insert(admin)
        return HandleAdmin.get_token(admin)

    @staticmethod
    def get_admin(username, password):
        admin = database.get_object(AdminAccount, (AdminAccount.get_username(AdminAccount) == username,
                                                   AdminAccount.get_password(AdminAccount) == sha256(password)))
        return admin

    def is_addmin(username):

        return database.find(AdminAccount, (AdminAccount.get_username(AdminAccount) == username, True))

    @staticmethod
    def create_new_tariff(**kwargs):
        new_tariff = AdminAccount.create_tariff(**kwargs)

        database.insert(new_tariff)
    @staticmethod
    def update_tariffs(tariff_id, **kwargs):
        tariff = database.get_object(Tariff, (Tariff.id == tariff_id, True))
        AdminAccount.change_tariff(**kwargs)


    @staticmethod
    def get_token(admin, expire_time=24):
        expire_delta = timedelta(expire_time)
        token = create_access_token(
            identity=admin.id, expires_delta=expire_delta)
        return token
    @staticmethod
    def get_list_of_tariffs():
        list_of_tariff = database.query(Tariff)
        return list_of_tariff