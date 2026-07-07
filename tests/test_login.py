import pytest
import allure

@allure.epic("Auth")
def test_login_failure(login_page):
    login_page.navigate()
    login_page.login('user', 'password')

    assert login_page.get_error_message() == 'Invalid credentials. Please try again.'

@pytest.mark.parametrize("username, password", [
    ("user", "user"),
    ("admin", "admin")
])
@allure.title("Test successful login")
@allure.description("User us able to login with username and password and redirected to the dashboard page after that")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_success(username, password, dashboard_page, login_page):
    with allure.step("Go to the login page"):
        login_page.navigate()
    with allure.step("Enter login and password"):
        login_page.login(username, password)
    with allure.step("Dashboard page is opened"):
        dashboard_page.assert_welcome_message("Welcome admin")
