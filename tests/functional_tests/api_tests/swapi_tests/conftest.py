import pytest

from core.swapi.swapi_ctrl import SwapiCtrl


@pytest.fixture(scope='session')
def swapi_ctrl() -> SwapiCtrl:
    swapi_ctrl = SwapiCtrl()
    return swapi_ctrl


@pytest.fixture(scope='session', autouse=True)
def clear_logs():
    yield
    file_name = 'pytest_logs.log'

    import pathlib

    # find all files with this name in project by using pathlib
    # delete file