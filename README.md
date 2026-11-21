# autotests-ui

Автоматизированное UI-тестирование QA-automation-engineer-ui-курса с использованием **Playwright** + **Pytest**.

## Архитектура

Проект следует **Page Object** и **Component Object** паттернам:

```
tests/        — тесты, сгруппированные по функциональным областям
pages/        — Page Object (страницы приложения)
components/   — Component Object (переиспользуемые компоненты страниц)
elements/     — базовые UI-элементы (кнопки, инпуты, ссылки и т.д.)
fixtures/     — pytest-фикстуры (браузеры, страницы)
testdata/     — тестовые данные и файлы
tools/allure/ — метаданные для Allure-отчётов (теги, эпик, фичи, истории)
practice/     — учебные примеры Pytest
playwright_examples/ — примеры использования Playwright API
```

## Установка

1. **Создать виртуальное окружение:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. **Установить зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Установить браузеры Playwright:**
   ```bash
   playwright install
   ```

## Запуск тестов

### PowerShell (Windows)
```powershell
.\run_tests.ps1
.\run_tests.ps1 -m regression
.\run_tests.ps1 -m courses
.\run_tests.ps1 --count 3          # запуск каждого теста 3 раза
.\run_tests.ps1 --browser chromium
```

### Прямой запуск
```bash
python -m pytest tests -v
python -m pytest tests -v --browser firefox
python -m pytest tests -v --count 2
```

### С фильтрацией по маркерам
- `regression` — регрессионные тесты
- `dashboard` — тесты рабочей панели
- `registration` — тесты регистрации
- `authorization` — тесты авторизации
- `courses` — тесты курсов

## Конфигурация

| Параметр    | Описание                                 |
|-------------|------------------------------------------|
| `--browser` | Браузер: `chromium`, `firefox`, `webkit` |
| `--count N` | Запустить каждый тест N раз              |
| `--headed`  | Запуск в видимом режиме                  |
| `--device`  | Эмуляция мобильного устройства           |

## Allure-отчёт

```bash
allure serve allure-results
```

## Зависимости

| Пакет                  | Версия | Назначение                     |
|------------------------|--------|--------------------------------|
| `playwright`           | 1.63.0 | UI-автоматизация               |
| `pytest`               | 9.1.1  | Фреймворк тестирования         |
| `pytest-playwright`    | 0.9.0  | Интеграция Playwright с Pytest |
| `pytest-base-url`      | 2.1.0  | Управление базовым URL         |
| `allure-pytest`        | 2.16.2 | Allure-отчёты                  |
| `pytest-rerunfailures` | 16.7   | Перезапуск упавших тестов      |
