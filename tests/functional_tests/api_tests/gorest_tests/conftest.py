import pytest

from core.gorest.gorest_ctrl import GorestCtrl


@pytest.fixture(scope='session')
def gorest_ctrl() -> GorestCtrl:
    gorest_ctrl = GorestCtrl()
    return gorest_ctrl

