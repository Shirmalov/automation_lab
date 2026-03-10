# Automation Lab
Лаборатория автоматизации тестирования: фреймворк для UI и API тестов с масштабируемой архитектурой, поддерживаемой структурой проекта, отчётностью и возможностью интеграции в CI/CD.

## Описание

Фреймворк предназначен для написания и запуска UI-тестов с применением паттерна Page Object Model (POM). Поддерживает генерацию отчётов Allure, параметризацию тестов и гибкую конфигурацию через маркеры pytest.

#### Структура проекта
```bash
automation_lab/
├── .venv/                  # Виртуальное окружение Python
├── base/                   # Базовые классы и утилиты
│   ├── __init__.py
│   ├── base_page.py        # Базовый класс для всех страниц (общие методы работы с элементами)
│   └── base_randomizer.py  # Утилиты для генерации случайных данных
│
├── config/                 # Конфигурационные файлы
│   ├── __init__.py
│   ├── data.py             # Константы и тестовые данные (логины, пароли)
│   └── links.py            # URL-адреса тестируемого приложения
│
├── data/                   # Модули для работы с данными
│   ├── __init__.py
│   ├── data_helper.py      # Вспомогательные функции для подготовки данных
│   └── user_role.py        # Описание ролей пользователей (enum или классы)
│
├── pages/                  # Page Objects (объекты страниц)
│   ├── admin/              # Страницы админ-панели
│   ├── __init__.py
│   └── login_page.py       # Объект страницы авторизации
│
├── tests/                  # Тестовые сценарии
│   ├── api/                # API тесты
│   ├── ui/                 # UI тесты
│   └── __init__.py
│
├── .env                    # Переменные окружения (секреты, конфиги)
├── .gitignore              # Файл игнорирования для Git
├── conftest.py             # Глобальные фикстуры и настройки Pytest
├── requirements.txt        # Список зависимостей проекта
├── setup.cfg               # Конфигурация инструментов (flake8, pytest и др.)
└── README.md               # Документация проекта
```


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