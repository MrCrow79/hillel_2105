import pytest

from test_functions_new import triangle_area


@pytest.mark.custom_mark_my_own
@pytest.mark.smoke
@pytest.mark.positive   # decorator
def tc_triangle_area_positive_all_1():
    assert round(triangle_area(1, 1, 1), 3) == 0.433


@pytest.mark.smoke
@pytest.mark.positive
def tc_triangle_area_positive_123():
    assert round(triangle_area(1, 2, 3), 3) == 0.0
