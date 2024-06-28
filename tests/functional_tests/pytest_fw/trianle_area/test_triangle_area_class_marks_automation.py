import os

import pytest

from condition import IS_DEV
from test_functions_new import triangle_area


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.class_tests
class TestTrianglePositive:

    @pytest.mark.xfail(reason='jira_issue_1, some description')
    def tc_class_triangle_area_positive_x_fail(self):
        assert round(triangle_area(0, 10, 10), 3) == 100.0

    @pytest.mark.xfail(reason='jira_issue_2, some description')
    def tc_class_triangle_area_positive_x_pass(self):
        pass

    @pytest.mark.skip(reason='jira_issue_3, some description')
    def tc_class_triangle_area_positive_skip(self):
        assert round(triangle_area(0, 10, 10), 3) == 100.0

    @pytest.mark.skipif(not IS_DEV, reason='Only for DEV')
    def tc_class_triangle_area_positive_skip_if(self):
        assert round(triangle_area(0, 10, 10), 3) == 100.0
