import pytest
from test_functions_new import triangle_area


@pytest.mark.negative
def tc_triangle_area_negative_all_0():
    assert round(triangle_area(0,0,0), 3) == 0.0


@pytest.mark.negative
def tc_triangle_area_negative_with_none():
    with pytest.raises(TypeError):
        assert round(triangle_area(None, 2, 3), 3) == 0.433
