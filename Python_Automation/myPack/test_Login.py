import pytest


@pytest.yield_fixture()
def setup():
    print('Open URL to Login')
    yield
    print('Close browser after Login')


def test_login_by_email(setup):
    print('This is login by email')


def test_login_by_facebook(setup):
    print('This is login by facebook')
