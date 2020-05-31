import pytest
from heysummit.api import HeySummit

def pytest_addoption(parser):
    '''
    register argparse-style options and ini-style config values.
    '''
    parser.addoption(
        '--token',
        action='store',
        help='Use token for tests'
    )


@pytest.fixture
def token(request):
    return request.config.getoption("--token")


@pytest.fixture
def hey(token):
    return HeySummit(token=token)