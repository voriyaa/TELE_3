from Runner import Authorization
from UserAccount import UserAccount
from HandleUser import HandleUser
from HandleAdmin import HandleAdmin


class Control:

    @staticmethod
    def control_in_out():
        while True:
            user_admin = Authorization.run()
            print(type(user_admin))
            if isinstance(user_admin, UserAccount):
                HandleUser.handle_user_actions(user_admin)
            else:
                HandleAdmin.handle_admin_actions(user_admin)
