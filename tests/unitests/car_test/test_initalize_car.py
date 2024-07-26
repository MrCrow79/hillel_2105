import pytest

# from .conftest import get_default_value  # relative path
from tests.unitests.car_test.conftest import get_default_value  # full path


@pytest.mark.xfail
@pytest.mark.parametrize('name', [
    'tank', 'fuel_consumption',  'engine_is_on', 'current_level_of_fuel'
])
def test_create_car_with_default_parameters(name, default_auto, fixture_for_example, fixture_postcondition):

    assert getattr(default_auto, name) == get_default_value(name)  # assert auto.name == expected_value, where name can be tank, fuel_consumption...
    # assert auto.__getattribute__(name) == expected_value  # assert auto.name == expected_value, where name can be tank, fuel_consumption...

