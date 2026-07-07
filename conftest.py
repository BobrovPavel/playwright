from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import pytest

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)