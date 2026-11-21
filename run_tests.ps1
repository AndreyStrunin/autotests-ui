# Запуск тестов в UTF-8, чтобы кириллица в выводе pytest не превращалась в кракозябры.
# Пример: .\run_tests.ps1 -m courses
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$OutputEncoding = [Console]::OutputEncoding
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

& "$PSScriptRoot\.venv\Scripts\python.exe" -m pytest @args
exit $LASTEXITCODE
