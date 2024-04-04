from src.Authorization.Authorization import Authorization
from src.User.UserAccount import UserAccount
from src.User.HandleUser import HandleUser
from src.Admin.HandleAdmin import HandleAdmin


class Control:

    @staticmethod
    def control_in_out():
        while True:
            user_admin = Authorization.run()
            while user_admin is None:
                user_admin = Authorization.run()
            if isinstance(user_admin, UserAccount):
                HandleUser.handle_user_actions(user_admin)
            else:
                HandleAdmin.handle_admin_actions(user_admin)
