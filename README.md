# Automation Lab
Лаборатория автоматизации тестирования: фреймворк для UI и API тестов с масштабируемой архитектурой, поддерживаемой структурой проекта, отчётностью и возможностью интеграции в CI/CD.

## Описание

Фреймворк предназначен для написания и запуска UI-тестов с применением паттерна Page Object Model (POM). Поддерживает генерацию отчётов Allure, параметризацию тестов и гибкую конфигурацию через маркеры pytest.

## Структура проекта
automation_lab/
├── requirements.txt # Зависимости проекта
├── README.md # Документация
├── conftest.py # Глобальные фикстуры pytest
├── core/
│ └── common/
│ ├── init.py
│ ├── base_page.py # Базовый класс для всех страниц
│ └── utils/
│ └── pytest_marks.py # Кастомные маркеры и декораторы
├── pages/
│ ├── init.py
│ └── login_page.py # Page Object для страницы авторизации
└── tests/
├── init.py
└── test_login_success.py # Тестовые сценарии


## Требования

- Python 3.11+
- Google Chrome
- ChromeDriver (устанавливается автоматически через webdriver-manager)

## Установка

### 1. Клонирование проекта

```bash
git clone <repository-url>
cd automation_lab
```

### 2. Создание виртуального окружения
```python3.11 -m venv .venv```

###  3. Активация виртуального окружения
```
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 4. Установка зависимостей
```
pip install -r requirements.txt
```

### 5. Проверка установки
```
pip list
```

### Содержимое requirements.txt
```
selenium>=4.15.0
pytest>=7.4.0
allure-pytest>=2.13.0
webdriver-manager>=4.0.0
pytest-metadata>=3.0.0
```

### Базовый запуск
```
pytest tests/test_login_success.py -v
```

### Запуск с генерацией Allure-отчёта
```
pytest tests/ -v --alluredir=allure-results
allure serve allure-results
```

### Запуск по маркерам
```
# Только smoke-тесты
pytest tests/ -v -m smoke

# Smoke и regress вместе
pytest tests/ -v -m "smoke or regress"

# Исключить flaky-тесты
pytest tests/ -v -m "not flaky"
```

### Дополнительные опции pytest
```
# Показать вывод print() в консоли
pytest -v -s

# Запуск с подробным логом
pytest -v --tb=short

# Остановиться после первого падения
pytest -x

# Повторить упавшие тесты (требует pytest-rerunfailures)
pytest --reruns 2 --reruns-delay 1
```