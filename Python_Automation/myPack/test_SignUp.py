import pytest


@pytest.yield_fixture()
def signin():
    print('Open URL to Login')
    yield
    print('Close browser after Login')


def test_sign_in_by_email(setup):
    print('This is sign in by email')


def test_sign_in_by_facebook(setup):
    print('This is sign in by facebook')

# SDET- QA Automation Techie - Selenium with Python Full Course For Beginners
