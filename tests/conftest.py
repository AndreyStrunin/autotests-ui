from typing import Any, Generator

import pytest
from playwright.sync_api import Page


@pytest.fixture
def chromium_page(playwright) -> Generator[Page, Any, None]:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()
