import pytest
import allure
import requests


@pytest.mark.smoke
@allure.title("Smoke Test report")
@allure.description("Smoke Test allure report")
@allure.tag("smoke")
def test_tc1():
    assert 1 + 1 == 2


@pytest.mark.smoke
def test_tc2():
    assert 1 + 1 == 3


@pytest.mark.reg
def test_tc3():
    assert 1 - 1 == 0
