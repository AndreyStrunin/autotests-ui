from pathlib import Path
from typing import Any, Generator

import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page

from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page

BROWSER_STATE_PATH = Path(__file__).resolve().parents[1] / "browser-state.json"


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Generator[Page, Any, None]:
    yield from initialize_playwright_page(playwright, test_name=request.node.name)


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    BROWSER_STATE_PATH.unlink(missing_ok=True)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.go_to("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration_form.fill_form(email='user.name@gmail.com', username='username',
                                                  password='password', )
    registration_page.click_registration_button()

    context.storage_state(path=BROWSER_STATE_PATH)
    browser.close()

    if not BROWSER_STATE_PATH.exists():
        raise RuntimeError(f"Не удалось сохранить состояние браузера: {BROWSER_STATE_PATH}")


@pytest.fixture(scope='function')
def chromium_page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Generator[
    Page, Any, None]:
    yield from initialize_playwright_page(playwright, test_name=request.node.name, store_state=BROWSER_STATE_PATH)
