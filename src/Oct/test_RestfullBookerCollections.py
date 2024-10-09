import pytest
import allure


@pytest.mark.smoke
@allure.title("Smoke Test report")
@allure.description("Smoke Test allure report")
@allure.tag("smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Ragul")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_tc1():
    assert 1 + 1 == 2


@pytest.mark.smoke
def test_tc2():
    assert 1 + 1 == 3


@pytest.mark.reg
def test_tc3():
    assert 1 - 1 == 0
