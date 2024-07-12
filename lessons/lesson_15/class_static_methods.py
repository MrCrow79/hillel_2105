from datetime import datetime

from utils.date_utils import DateUtils


class PhoneBase:

    def __init__(self, label, model, cpu, ram, memory, os):
        self.label = label
        self.model = model
        self.cpu = cpu
        self.ram = ram
        self.memory = memory
        self.os = os

    def start_call(self):
        raise NotImplementedError('Method is not implemented')

    def send_sms(self):
        raise NotImplementedError('Method is not implemented')

    def get_info(self):
        return f'{self.label}, {self.model}, {self.os}'


class Apple11(PhoneBase):

    def __init__(self, cpu, ram, memory):
        super().__init__(label='Apple', model='11x', cpu=cpu, ram=ram, memory=memory, os='iOS')
        self.next_year = DateUtils.get_next_year()


    def send_sms(self):
        print(f'Sending sms from {__class__.__name__}')


class Android(PhoneBase):

    android_label = ['Android base']

    def __init__(self, label, model, cpu, ram, memory):
        super().__init__(label=label, model=model, cpu=cpu, ram=ram, memory=memory, os='Android')

    @classmethod
    def start_call(cls):
        print(f'Start calling from {__class__.__name__}')
        print(f'Start calling from {cls.android_label}')


class OnePlus8Pro(Android):

    def __init__(self):
        super().__init__(label=['One_plus'], model='8 pro', cpu='3.0', ram='8', memory='256')

    def send_sms(self):
        print(f'Sending sms from {self.model}, {self.label}')



if __name__ == '__main__':
    pass
    # a11x = Apple11('2.0', 8, 128)
    # a11x.send_sms()

    # op8p = OnePlus8Pro()
    # op8p_second = OnePlus8Pro()
    #
    # print(id(op8p.android_label))
    # print(id(op8p_second.android_label))
    # print(id(OnePlus8Pro.android_label))
    #
    # print('-' * 80)
    # OnePlus8Pro.android_label = ['asd']
    #
    # print(id(op8p.android_label))
    # print(id(op8p_second.android_label))
    # print(id(OnePlus8Pro.android_label))
    #
    # print('-' * 80)
    #
    # # print(id(op8p.label))
    # # print(id(op8p_second.label))
    # # print('-' * 80)
    # # op8p.android_label = 'New value'
    #
    # print('-' * 80)
    # op8p.android_label = 'New value'
    # print(id(op8p.android_label))
    # print(id(op8p_second.android_label))
    # print(id(OnePlus8Pro.android_label))
    #
    # print('-' * 80)
    # print(op8p.android_label)
    # op8p.__class__.android_label = 'change by __clas__ var'
    # print(op8p.__class__.android_label)
    # print(OnePlus8Pro.android_label)


    # op8p.start_call()

    # print('8pro label', op8p.label)
    # print('8pro android_label', op8p.android_label)
    #
    # print('op8p_second label', op8p_second.label)
    # print('op8p_second android_label', op8p_second.android_label)
    #
    #
    #
    #
    # op8p.label = 'New label for op8p'
    # print('8pro label', op8p.label)
    # print('op8p_second label', op8p_second.label)
    # print('-' * 80)
    # # op8p.android_label = 'New android label for class'
    # # print('8pro label', op8p.android_label)
    # # print('op8p_second label', op8p_second.android_label)
    #
    # OnePlus8Pro.android_label = 'New android label for class'
    # print('8pro label', op8p.android_label)
    # print('op8p_second label', op8p_second.android_label)




    # print(datetime.now())
    #
    # print(DateUtils.get_current_year('2020-04-04'))
    # print(DateUtils.get_next_year())
    # print(datetime.now())
    # print(DateUtils().get_next_year())
    # print(datetime.now())


