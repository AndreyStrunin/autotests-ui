def test_user_login():
    print('test_user_login')


class TestUserLogin:
    def test_user_login(self):
        print('test_user_login')

    def test_user_logout(self):
        print('test_user_logout')

def test_first_try():  # Этот тест мы добавили в предыдущем шаге
    print("Hello World!")


def test_assert_positive_case():  # Новый тест, которые проверяет положительный кейс
    assert (2 + 2) == 4  # Ожидается, что тест пройдет


def test_assert_negative_case():  # Новый тест, которые проверяет негативный кейс
    assert (2 + 3) == 5  # Тут должна быть ошибка