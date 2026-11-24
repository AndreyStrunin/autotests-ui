from re import Pattern

import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def go_to(self, url: str):
        with allure.step(f"Go to {url}"):
            self.page.goto(url, wait_until="domcontentloaded")

    def reload_page(self):
        with allure.step(f"Reload page {self.page.url}"):
            self.page.reload(wait_until="domcontentloaded")

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f"Check the current url {expected_url.pattern}"):
            expect(self.page).to_have_url(expected_url)
