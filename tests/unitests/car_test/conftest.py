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
    yield auto  # returns auto

    # next rows will be executed after test
    del auto
    print('Autto was deleted')


@pytest.fixture  # will be run fot each test
def fixture_for_example(default_tank, default_fuel_consumption):
    print('fixture_for_example before test')
    yield   # return None
    print('fixture_for_example after test')


@pytest.fixture  # will be run fot each test
def fixture_postcondition():
    yield   # return None
    print('fixture_postcondition after test')