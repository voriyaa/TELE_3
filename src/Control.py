from Runner import Authorization
from UserAccount import UserAccount
from HandleUser import HandleUser
from HandleAdmin import HandleAdmin


class Control:

    @staticmethod
    def control_in_out():
        while True:
            user_admin = Authorization.run()
            if isinstance(user_admin, UserAccount):
                user_admin = HandleUser(user_admin.get_first_name(), user_admin.get_last_name(),
                                        user_admin.get_birth_data(), user_admin.get_passport_id(),
                                        user_admin.get_sex(), user_admin.get_username(),
                                        user_admin.get_password(), user_admin.get_phone_number())
                user_admin.handle_user_actions()
            else:
                user_admin = HandleAdmin(user_admin.get_first_name(), user_admin.get_last_name(),
                                         user_admin.get_birth_data(), user_admin.get_passport_id(),
                                         user_admin.get_sex(), user_admin.get_username(),
                                         user_admin.get_password(), user_admin.get_phone_number())
                user_admin.handle_admin_actions()
