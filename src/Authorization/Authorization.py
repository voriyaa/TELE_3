from hashlib import sha256
from src.User.UserAccount import UserAccount
from src.Admin.AdminAccount import AdminAccount, Tariff
from src.Tools.DataBase import database
from dotenv import load_dotenv
from src.Tools.MyHashFunc import HashFunction
import os

load_dotenv()
class Authorization:
    @staticmethod
    def admin_login(username, password):
        return database.find(AdminAccount, (
        AdminAccount.get_username(AdminAccount) == username, AdminAccount.get_password(AdminAccount) == password))

    @staticmethod
    def user_login(username, password):
        return database.find(UserAccount, (
            UserAccount.get_username(UserAccount) == username, UserAccount.get_password(UserAccount) == password))

