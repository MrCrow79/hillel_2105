from pytest import fixture

@fixture(scope='session', autouse=True)
def read_envs():
    from utils.setting_utils import settings