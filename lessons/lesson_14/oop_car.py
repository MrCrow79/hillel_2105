
class Auto:
    def __init__(self, engine, model, label, tank, year):  # engine, label, model, tank, year
        self.engine = engine
        self.label = label
        self.model = model
        self.tank = tank
        self.year = year
        self.owner_name = 'unknown'

    def say_label(self):
        print(f'I\'m {self.label}')

    def set_tank(self, tank):
        self.tank = tank

    def say_class_name(self):
        print('I\'m Auto')

    def say_hi(self, name):
        print(f'Hi {name}')


class Lexus(Auto):  # inheritance

    def __init__(self, engine, model, tank, year):  # engine, label, model, tank, year
        super().__init__(engine=engine, model=model, label='Lexus', tank=tank, year=year)  # call __init__ from Auto
        self.model_new = f'Lexus {self.model}'
        self.owner_name = 'japan'
        # Auto(engine, model, 'Lexus', tank, year)  # call __init__ from Auto

    def say_class_name(self):  # re-initialization
        print('I\'m Lexus')


class CX40(Lexus):  # inheritance

    def __init__(self, year):  # engine, label, model, tank, year
        super().__init__(engine='2.0', model='cx40', tank='45', year=year)  # call __init__ from Lexus
        # super(__class__).__init__(engine='2.0', model='cx40', tank='45', year=year)  # call __init__ from Lexus
        self.model_new = f'Lexus {self.model}'


class Tesla(Auto):  # inheritance

    def __init__(self, model, tank, year):  # engine, label, model, tank, year
        super().__init__(engine='-', model=model, label='Tesla',
                         tank=tank, year=year)  # call __init__ from Auto
        self.engine_type = 'electro'
        # Auto(engine, model, 'Lexus', tank, year)  # call __init__ from Auto

    def say_class_name(self):
        print('I\'m Tesla')


# inheritance
# Incapsulation
# Polimorfism

crx_65_auto = Auto('2.0', 'crx_40', 'Lexus', '55', 2015)
crx_40 = Lexus('2.0', 'crx_40', '45', '2015')
crx_50 = Lexus('2.6', 'crx_50', '42', '2017')
ct = Tesla(model='ct', tank=0, year=2020)
cx_40_new = CX40(2020)

cx_40_new.say_class_name()
cx_40_new.set_tank(50)
print('cx_40_new print tank', cx_40_new.tank)

print('Auto class', crx_65_auto.owner_name)
print('Lexus class', crx_40.owner_name)
print('CX40 class', cx_40_new.owner_name)
print('Tesla class', ct.owner_name)

# crx_40.say_class_name()
# ct.say_class_name()
# cx_40_new.say_class_name()

# ct.say_hi('Alex')
# cx_40_new.say_hi('Ivamn')

# print(crx_50.tank)
# crx_50.set_tank(90)
# print(crx_50.tank)
# print(crx_50.model)
# print(crx_50.model_new)
#
# print(ct.engine_type)
# print(ct.tank)
#
# ct.set_tank(20)
#
# cx_40_new = CX40(2020)
#
# cx_40_new.set_tank(90)
# print(cx_40_new.tank)