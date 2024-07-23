from lessons.lesson_17.car_class_example import Auto
import pytest


def get_default_value(name):
    return {
        'tank': _default_tank(),
        'engine_is_on': False,
        'fuel_consumption': _default_fuel_consumption(),
        'current_level_of_fuel': _default_tank(),
    }[name]


def _default_tank():
    return 300


def _default_fuel_consumption():
    return 0.25

@pytest.fixture(scope='session')  # will be run once
def default_tank():
    return _default_tank()


@pytest.fixture(scope='session')  # will be run once
def default_fuel_consumption():
    return _default_fuel_consumption()


@pytest.fixture(scope='session')  # will be run once
def default_auto(default_tank, default_fuel_consumption):
    print('Creating autooo')
    auto = Auto(tank=default_tank, fuel_consumption=default_fuel_consumption)
    return auto