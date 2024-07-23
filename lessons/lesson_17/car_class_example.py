class Auto:

    def __init__(self, tank: int | float, fuel_consumption: int | float):
        self.tank = self.__check_value_more_than_0(tank, 'tank')
        self.fuel_consumption = self.__check_value_more_than_0(fuel_consumption, 'fuel_consumption')
        self.engine_is_on = False
        self.current_level_of_fuel = tank

    @staticmethod
    def __check_value_more_than_0(value: int, name):
        if not isinstance(value, (int, float)):
            raise TypeError(f'Value of {name} shout be int or float')

        if value <= 0:
            raise ValueError(f'Value of {name} should be greate than 0')

        return value

    def start(self):
        if self.engine_is_on:
            self.__turn_on_engine()
        else:
            raise PermissionError('You can\'t turn on engine if it\'s already on')

    def drive(self, km=0):
        can_drive = self.current_level_of_fuel / self.fuel_consumption
        if can_drive >= km:

            self.current_level_of_fuel = self.current_level_of_fuel - km / self.fuel_consumption

            msg = f'Driving {km}'
            print(msg)
            return msg

        else:

            msg = f'Not enough fuel for driving  {km}'
            print(msg)
            return msg

    def __turn_on_engine(self):
        self.engine_is_on = True

    def __turn_off_engine(self):
        self.engine_is_on = False

    def stop(self):
        if self.engine_is_on is False:
            self.__turn_off_engine()
        else:
            raise PermissionError('You can\'t turn off engine if it\'s already off')
