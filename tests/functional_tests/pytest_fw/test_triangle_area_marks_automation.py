import os

import pytest

from condition import IS_DEV
from test_functions_new import triangle_area


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.xfail(reason='jira_issue_1, some description')
def tc_triangle_area_positive_x_fail():
    assert round(triangle_area(0, 10, 10), 3) == 100.0


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.xfail(reason='jira_issue_2, some description')
def tc_triangle_area_positive_x_pass():
    pass


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.skip(reason='jira_issue_3, some description')
def tc_triangle_area_positive_skip():
    assert round(triangle_area(0, 10, 10), 3) == 100.0


@pytest.mark.smoke
@pytest.mark.positive
# @pytest.mark.skipif(os.getenv('CUR_DB', None) != 'POSTGRES', reason='Only for postgres')
@pytest.mark.skipif(not IS_DEV, reason='Only for DEV')
def tc_triangle_area_positive_skip_if():
    assert round(triangle_area(0, 10, 10), 3) == 100.0


@pytest.mark.smoke
@pytest.mark.positive
def tc_triangle_area_positive_skip_inside():
    pytest.skip('Only for DEV')
    # assert round(triangle_area(0, 10, 10), 3) == 100.0
