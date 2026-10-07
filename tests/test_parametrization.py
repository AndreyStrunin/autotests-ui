import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 2, 3])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])  # Параметризируем по операционной системе
@pytest.mark.parametrize("browser", ["chromium", "webkit", "firefox"])  # Параметризируем по браузеру
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0  # Проверка указана для примера])


@pytest.fixture(params=["chromium", "webkit", "firefox"])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser):
    print(f'Running test: {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f'Running test with: {user} ')

    def test_user_without_operations(self, user: str):
        print(f'Running test without: {user} ')
