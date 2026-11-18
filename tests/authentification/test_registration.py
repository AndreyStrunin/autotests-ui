import allure
import pytest

from pages.authentification.registration_page import RegistrationPage
from pages.dashdoard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag



@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGISTRATION, AllureTag.REGISTRATION)
class TestRegistration:
    @allure.title("Registration with correct username and password")
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.go_to("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill_form(
            email="user.name@gmail.com",
            username="username",
            password="password"
        )
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()