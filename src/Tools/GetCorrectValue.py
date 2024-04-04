class GetCorrectValue:
    @staticmethod
    def get_number(min_value=0, max_value=9999999999, **args):
        number = input(args['first_out'])
        while not (number.isdigit() and min_value <= int(number) <= max_value):
            number = input(args['second_out'])
        return int(number)
