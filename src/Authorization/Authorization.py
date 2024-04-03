# -*- coding: utf-8 -*-
from hashlib import sha256
from src.Constants.Constants import Constant
from dotenv import load_dotenv
from src.Authorization.AdminAuthorization import AdminAuthorization
from src.Authorization.UserAuthorization import UserAuthorization
from src.Tools.GetCorrectValue import GetCorrectValue


def sha256_str(item):
    return sha256(str(item).encode()).hexdigest()


load_dotenv()

# DATABASE_URL = 'postgresql://postgres:123@192.168.0.105:5432/test'
"""db_file = 'example.db'

DATABASE_URL = f'sqlite:///{db_file}'

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)
s = session()
"""


class Authorization:

    @staticmethod
    def run():
        print(Constant.HI_TO_USER)

        variant = GetCorrectValue.get_number(min_value=1,
                                             max_value=2,
                                             first_out=Constant.CHOOSE_STATUS,
                                             second_out=Constant.CHOOSE_OPTION)

        if variant == 1:
            return AdminAuthorization.admin_workflow()
        else:
            return UserAuthorization.user_workflow()
