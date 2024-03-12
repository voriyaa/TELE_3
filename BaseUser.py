class BaseUser:

    def __init__(self, first_name: str, last_name: str,
                 birth_date: str, passport_id: int, sex: str) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birth_date = birth_date
        self.__passport_id = passport_id
        self.__sex = sex

    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def get_birth_data(self) -> str:
        return self.__birth_date

    def get_passport_id(self) -> int:
        return self.__passport_id

    def get_sex(self) -> str:
        return self.__sex







