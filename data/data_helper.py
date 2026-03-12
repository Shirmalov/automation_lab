import json
import random
import string
from datetime import date, datetime, timedelta
from decimal import Decimal
from pathlib import Path
from typing import Any, Optional
from zoneinfo import ZoneInfo
from dataclasses import dataclass

from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

from base.base_randomizer import BaseRandomizer


__all__ = ['data_helper', 'DataHelper', 'ActData']


@dataclass
class ActData:
    amount_without_vat: float
    vat_rate: int
    vat_amount: float
    total_amount: float


class DataHelper(BaseRandomizer):

    def __init__(self):
        super().__init__()
        self.tz = ZoneInfo('Europe/Moscow')

    @staticmethod
    def get_discount_sum(part: int | float, total: int | float) -> float:
        """
        Получить итоговую сумму с учетом скидки.

        >>> dh = DataHelper()
        >>> dh.get_discount_sum(10, 100)
        90.0
        >>> dh.get_discount_sum(25, 30)
        22.5
        """
        percentage = total - (part * total) / 100
        return percentage

    def is_afternoon(self) -> bool:
        """Return True if current time is afternoon."""
        now = datetime.now(tz=self.tz)
        return now.hour >= 12

    @staticmethod
    def get_random_date(start: datetime, end: datetime = None, format_string: str = '%d.%m.%Y'):
        """Return a random datetime between two datetime objects."""
        if end is None:
            end = datetime.now()
        delta = end - start
        random_value = random.choice(range(delta.days)) if delta.days > 0 else random.choice(range(delta.days, 0))
        _date = start + timedelta(random_value)
        return _date.strftime(format_string)

    @staticmethod
    def get_current_year() -> str:
        """Возвращает текущий год."""
        return datetime.now().strftime('%Y')

    @staticmethod
    def is_last_month_day() -> bool:
        """Определить, является ли текущая дата последним днем месяца."""
        current_date = datetime.now()
        last_day = current_date + relativedelta(day=31)
        return current_date == last_day

    def get_current_date_with_tz(self, format_string: str = '%d.%m.%Y', tz: ZoneInfo | None = None) -> str:
        return datetime.now(tz=tz or self.tz).strftime(format_string)

    @staticmethod
    def get_current_date(format_string: str = '%d.%m.%Y') -> str:
        return datetime.now().strftime(format_string)

    @staticmethod
    def get_future_date(day_plus: int, format_string: str = '%d.%m.%Y'):
        """Получить будущую дату в {day_plus} от текущего дня."""
        return (datetime.now() + timedelta(days=day_plus)).strftime(format_string)

    @staticmethod
    def get_random_date_current_year(format_string: str = '%d.%m.%Y'):
        today = date.today()
        start_of_year = date(today.year, 1, 1)
        days_range = (today - start_of_year).days + 1
        random_offset = random.randint(0, days_range - 1)
        random_date = start_of_year + timedelta(days=random_offset)

        return random_date.strftime(format_string)

    @staticmethod
    def get_random_period_current_year(format_string: str = '%d.%m.%Y') -> tuple[str, str]:
        today = date.today()
        start_of_year = today.replace(month=1, day=1)
        days_range = (today - start_of_year).days + 1
        day_start = random.randint(0, days_range - 1)
        day_end = random.randint(day_start, days_range - 1)
        date_start = (start_of_year + timedelta(days=day_start)).strftime(format_string)
        date_end = (start_of_year + timedelta(days=day_end)).strftime(format_string)

        return date_start, date_end

    @staticmethod
    def get_past_date(day_minus: int, format_string: str = '%d.%m.%Y'):
        """Получить прошлую дату в {day_minus} от текущего дня."""
        return (datetime.now() - timedelta(days=day_minus)).strftime(format_string)

    def get_past_period(self, max_days: int = 365) -> tuple[str, str]:
        """Получить случайный период в прошлом."""
        end_day_minus = self.random_number(1, max_days)
        start_day_minus = self.random_number(end_day_minus, max_days)
        start_date = self.get_past_date(start_day_minus)
        end_date = self.get_past_date(end_day_minus)
        return start_date, end_date

    @staticmethod
    def get_next_date(format_string: str = '%d.%m.%Y') -> str:
        """Получить следующую дату от текущего дня."""
        return (datetime.now() + timedelta(days=1)).strftime(format_string)

    @staticmethod
    def get_previous_date(format_string: str = '%d.%m.%Y') -> str:
        """Получить предыдущую дату от текущего дня."""
        return (datetime.now() + timedelta(days=-1)).strftime(format_string)

    @staticmethod
    def get_next_day_number() -> str:
        """Получить номер следующего дня от текущей даты."""
        day = (datetime.now() + timedelta(days=1)).strftime('%d')
        return str(int(day))  # убираем лидирующий ноль

    @staticmethod
    def get_previous_day_number() -> str:
        """Получить номер предыдущего дня от текущей даты."""
        day = (datetime.now() + timedelta(days=-1)).strftime('%d')
        return str(int(day))  # убираем лидирующий ноль

    @staticmethod
    def get_next_date_after_required_date(date_string: str, format_string: str = '%d.%m.%Y') -> str:
        """Метод возвращает следующую дату после нужной (переданной) даты."""
        _date = datetime.strptime(date_string, format_string)
        next_date = _date + timedelta(days=1)
        return next_date.strftime(format_string)

    @staticmethod
    def get_date_after_required_date(date_string: str, days: int, format_string: str = '%d.%m.%Y') -> str:
        """Метод возвращает дату после нужной (переданной) даты."""
        _date = datetime.strptime(date_string, format_string)
        new_date = _date + timedelta(days=days)
        return new_date.strftime(format_string)

    @staticmethod
    def add_month_to_date(date_string: str, month: int, format_string: str = '%d.%m.%Y'):
        """Добавляет указанное количество месяцев к переданной дате."""
        _date = datetime.strptime(date_string, format_string)
        new_date = _date + relativedelta(months=month)
        return new_date.strftime(format_string)

    @staticmethod
    def get_csv_data_from_file(*relative_path: str) -> list[list[str]]:
        base_dir = Path(__file__).parent.parent.parent / 'core' / 'resources'
        absolute_path = base_dir.joinpath(*relative_path)
        rows = []
        with open(absolute_path, 'r') as f:
            for line in f:
                # strip whitespace
                line = line.strip()
                # separate the columns
                line = line.split(',')
                rows.append(line)
        return rows

    @staticmethod
    def get_text_from_file(*relative_path: str) -> str:
        base_dir = Path(__file__).parent.parent.parent / 'core' / 'resources'
        absolute_path = base_dir.joinpath(*relative_path)
        with open(absolute_path, 'rb') as f:
            text = f.read().decode('utf-8')
            return text

    @staticmethod
    def get_json_file_data(*relative_path: str) -> dict:
        base_dir = Path(__file__).parent.parent.parent / 'core' / 'resources'
        absolute_path = base_dir.joinpath(*relative_path)
        with open(absolute_path, 'r') as f:
            data = json.load(f)
            return data

    @staticmethod
    def get_json_string_data(string: str) -> dict[Any]:
        return json.loads(string)

    @staticmethod
    def get_absolute_path_path(*relative_path: str, main_dir: str = 'resources') -> Path:
        base_dir = Path(__file__).parent.parent.parent / 'core' / main_dir
        absolute_path = base_dir.joinpath(*relative_path)
        return absolute_path

    @staticmethod
    def format_phone_number(phone: str, is_plus: bool = True):
        """
        Форматирует номер телефона '7xxxxxxxxxx' в строку '+7 xxx xxx xx xx'.

        >>> dh = DataHelper()
        >>> dh.format_phone_number('79032910803')
        '+7 903 291 08 03'
        """
        numbers = list(filter(str.isdigit, phone))[1:]
        mask = '7 {}{}{} {}{}{} {}{} {}{}'
        if is_plus:
            mask = f'+{mask}'
        return mask.format(*numbers)

    @staticmethod
    def format_phone_number_with_hyphen(phone: str):
        """
        Форматирует номер телефона '7xxxxxxxxxx' в строку '+7 xxx xxx-xx-xx'.

        >>> dh = DataHelper()
        >>> dh.format_phone_number_with_hyphen('79032910803')
        '+7 903 291-08-03'
        """
        numbers = list(filter(str.isdigit, phone))[1:]
        return '+7 {}{}{} {}{}{}-{}{}-{}{}'.format(*numbers)

    def get_data_from_xml_file(self, *relative_path: str, **kwargs) -> str:
        """
        Получение данных из xml-файла.

        Возможно предварительно форматирование. Возвращает текст.
        """
        text = self.get_text_from_file(*relative_path)
        if kwargs:
            text = self.format_text(text, **kwargs)
        return text

    def parse_date(self, date_string: str, **kwargs) -> date:
        """
        Парсит строку с датой и переводит в объект datetime.

        Внимание! Если дата в формате "dd.mm.YYYY", то нужно указывать аргумент dayfirst=True
        timezone issue: https://www.linux.org.ru/forum/development/13640755
        :param date_string: str
        :return: datetime
        """
        return parse(date_string, **kwargs).replace(tzinfo=self.tz).date()

    def parse_datetime(self, datetime_string: str, timezone=None, **kwargs) -> datetime:
        """
        Парсит строку с датой и временем и переводит в объект datetime.

        Внимание! Если дата в формате "dd.mm.YYYY", то нужно указывать аргумент dayfirst=True
        timezone issue: https://www.linux.org.ru/forum/development/13640755
        :param datetime_string: str
        :param timezone: tzinfo
        :return: datetime
        """
        if timezone is None:
            timezone = self.tz
        else:
            timezone = ZoneInfo(timezone)
        return parse(datetime_string, **kwargs).astimezone(tz=timezone)

    def reformat_date(self, date_string: str, format_string: str = '%d.%m.%Y', **kwargs: Any) -> str:
        """
        Принимает строку с датой, переформатирует в указанный формат.

        Внимание! Если дата в формате "dd.mm.YYYY", то нужно указывать аргумент dayfirst=True
        """
        return self.parse_date(date_string, **kwargs).strftime(format_string)

    def reformat_datetime(
            self,
            datetime_string: str,
            format_string: str = '%d.%m.%Y %H:%M:%S',
            timezone=None,
            **kwargs: Any
    ) -> str:
        """
        Принимает строку с датой и временем и переформатирует в указанный формат.

        Внимание! Если дата в формате "dd.mm.YYYY", то нужно указывать аргумент dayfirst=True
        >>> dh = DataHelper()
        >>> dh.reformat_datetime('2022-12-01 17:09:42.758237+00:00')
        '01.12.2022 20:09:42'
        >>> dh.reformat_datetime('2022-12-01 15:00:54.158237+03:00')
        '01.12.2022 15:00:54'
        >>> dh.reformat_datetime('2022-12-01 23:00:00.258237+00:00')
        '02.12.2022 02:00:00'
        """
        return self.parse_datetime(datetime_string, timezone=timezone, **kwargs).strftime(format_string)

    def calculate_age(self, birthday: str, **kwargs) -> int:
        """
        Рассчитывает количество полных лет.

        Внимание! Если дата в формате "dd.mm.YYYY", то нужно указывать аргумент dayfirst=True
        :param birthday: str
            - дата рождения
        :param kwargs: Any
              - см доку по dateutil.parser.parse
        :return: int
        """
        born = self.parse_date(birthday, **kwargs)
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    @staticmethod
    def get_plural_age(age: int) -> str:
        """Возвращает корректную форму существительного (год, года, лет) в зависимости от значения возраста."""
        count = age % 100
        if 5 <= count <= 20:
            text = 'лет'
        else:
            count = count % 10
            if count == 1:
                text = 'год'
            elif 2 <= count <= 4:
                text = 'года'
            else:
                text = 'лет'
        return text

    def calculate_age_with_noun(self, birthday: str, **kwargs) -> str:
        """
        Рассчитывает количество полных лет и форму существительного (год, года, лет).

        Внимание! Если дата в формате "dd.mm.YYYY", то нужно указывать аргумент dayfirst=True
        :param birthday: str
            - дата рождения
        :param kwargs: Any
              - см доку по dateutil.parser.parse
        :return: str
        """
        age = self.calculate_age(birthday, **kwargs)
        return f'{age} {self.get_plural_age(age)}'

    @staticmethod
    def short_fio(full_fio: str) -> str:
        """Заменяет полное фио на фамилию + инициалы."""
        last_name, first_name, middle_name = full_fio.split()
        return f'{last_name} {first_name[0]}. {middle_name[0]}.'

    @staticmethod
    def get_fio_string(profile):
        """Возвращает строку с полным ФИО по данным профиля."""
        data_list = [profile.surname, profile.name, profile.patronymic]
        data_list = [item for item in data_list if item is not None]
        return ' '.join(data_list)

    @staticmethod
    def get_fio_lat_string(profile):
        """Возвращает строку с полным ФИО на латинском по данным профиля."""
        data_list = [profile.surnameLatin, profile.nameLatin, profile.patronymicLatin]
        data_list = [item for item in data_list if item is not None]
        return ' '.join(data_list)

    @staticmethod
    def get_fio_string_with_line_break(profile):
        """
        Возвращает строку с полным ФИО по данным профиля.

        При полном ФИО возвращает строку с переносом: 1 - фамилия, 2 - имя и отчество;
        при неполном: одну строку.
        """
        data_list = [profile.surname, profile.name, profile.patronymic]
        data_list = [item for item in data_list if item is not None]
        if len(data_list) == 3:
            return f'{data_list[0]}\n{data_list[1]} {data_list[2]}'
        return ' '.join(data_list)

    @staticmethod
    def get_file_binary_data(full_path: str) -> bytes:
        with open(full_path, 'rb') as f:
            return f.read()

    @staticmethod
    def calc_price_without_nds(value: Decimal, tax=0.2, round_value: int = 2) -> Decimal:
        """
        Рассчитать стоимость без НДС.

        >>> dh = DataHelper()
        >>> dh.calc_price_without_nds(Decimal(100))
        Decimal('83.33')
        >>> dh.calc_price_without_nds(Decimal(1.5))
        Decimal('1.25')
        >>> dh.calc_price_without_nds(Decimal(1666.5))
        Decimal('1388.75')
        """
        return round(value / Decimal(1 + tax), round_value)

    @staticmethod
    def random_url():
        subdomain = ''.join(random.choices(string.ascii_lowercase, k=7))
        domains = ['ru', 'com', 'net', 'org']
        chosen_domain = random.choice(domains)
        url = f'https://{subdomain}.{chosen_domain}'
        return url

    @staticmethod
    def generate_random_phone():
        return '7' + ''.join([str(random.randint(0, 9)) for _ in range(10)])

    @staticmethod
    def generate_kpp():
        """
        Генерирует случайный валидный КПП (9 знаков) в формате.

        - первые 4 цифры - код налогового органа (от 1000 до 9999)

        - 5 и 6 цифры - причина постановки (от 01 до 50)

        - последние 3 цифры - порядковый номер (от 001 до 999)
        """
        # Код налогового органа (4 цифры)
        tax_code = f'{random.randint(1000, 9999):04d}'  # todo: после фикса вернуть ведущие нули

        # Код причины постановки (2 цифры, основные варианты)
        reason_codes = ['01', '02', '03', '04', '05', '06', '07', '08',
                        '09', '10', '11', '12', '13', '14', '15', '16',
                        '31', '32', '33', '34', '35', '36', '37', '38',
                        '39', '40', '41', '42', '43', '44', '45', '46',
                        '47', '48', '49', '50']
        reason_code = random.choice(reason_codes)

        # Порядковый номер (3 цифры)
        serial_number = f'{random.randint(1, 999):03d}'

        return f'{tax_code}{reason_code}{serial_number}'

    @staticmethod
    def generate_legal_person_inn() -> str:
        """Генерирует валидный ИНН юридического лица (10 цифр) с проверкой контрольных сумм по алгоритму ФНС."""
        inn = [random.randint(1, 9)]
        inn += [random.randint(0, 9) for _ in range(8)]

        # Расчет контрольной суммы (10-я цифра)
        weights = [2, 4, 10, 3, 5, 9, 4, 6, 8]
        control_sum = sum(w * n for w, n in zip(weights, inn)) % 11
        control_digit = control_sum % 10 if control_sum < 10 else 0
        inn.append(control_digit)

        return ''.join(map(str, inn))

    @staticmethod
    def generate_physical_person_ip_inn() -> str:
        """Генерирует валидный ИНН физ. лица и ИП (12 цифр) с проверкой контрольных сумм по алгоритму ФНС."""
        # Первые 10 цифр (регистрационный номер)
        inn = [random.randint(1, 9)]
        inn += [random.randint(0, 9) for _ in range(9)]

        # Расчет первой контрольной суммы (11-я цифра)
        weights1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
        control_sum1 = sum(w * n for w, n in zip(weights1, inn)) % 11
        control_digit1 = control_sum1 % 10 if control_sum1 < 10 else 0
        inn.append(control_digit1)

        # Расчет второй контрольной суммы (12-я цифра)
        weights2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
        control_sum2 = sum(w * n for w, n in zip(weights2, inn)) % 11
        control_digit2 = control_sum2 % 10 if control_sum2 < 10 else 0
        inn.append(control_digit2)

        return ''.join(map(str, inn))

    @staticmethod
    def format_all_amount(amount: int | float) -> str:
        """
        Форматирует числовую сумму с пробелами как разделителями тысяч и двумя знаками после запятой.

        Примеры:
            format_amount(100)      → '100.00'
            format_amount(1000)     → '1 000.00'
            format_amount(1234567)  → '1 234 567.00'
            format_amount(1234.5)   → '1 234.50'

        :param amount: Число (int или float)
        :return: Строка в формате 'X XXX.XX'
        """
        value = float(amount)
        formatted = f'{value:.2f}'
        integer_part, decimal_part = formatted.split('.')
        reversed_int = integer_part[::-1]
        grouped = ' '.join(reversed_int[i:i + 3] for i in range(0, len(reversed_int), 3))
        formatted_integer = grouped[::-1]

        return f'{formatted_integer}.{decimal_part}'

    @staticmethod
    def format_amount_statistics(amount: int | float) -> str:
        value = float(amount)
        formatted = f'{value:.2f}'
        integer_part, decimal_part = formatted.split('.')
        reversed_int = integer_part[::-1]
        grouped = ' '.join(reversed_int[i:i + 3] for i in range(0, len(reversed_int), 3))
        formatted_integer = grouped[::-1]
        decimal_part = decimal_part.rstrip('0')

        if not decimal_part:
            return formatted_integer

        return f'{formatted_integer}.{decimal_part}'

    @staticmethod
    def format_amount_in_table(amount: int | float) -> str:
        value = float(amount)
        formatted = f'{value:.2f}'
        integer_part, decimal_part = formatted.split('.')
        reversed_int = integer_part[::-1]
        grouped = ' '.join(reversed_int[i:i + 3] for i in range(0, len(reversed_int), 3))
        formatted_integer = grouped[::-1]

        if decimal_part == '00':
            return formatted_integer

        return f'{formatted_integer}.{decimal_part}'

    @staticmethod
    def generate_act_data(
            vat_rate: Optional[int] = None,
            amount_without_vat: Optional[float] = None,
    ) -> ActData:
        allowed_vat_rates = (0, 5, 7, 10, 20, 22)
        if vat_rate is None:
            vat_rate = random.choice(allowed_vat_rates)
        elif vat_rate not in allowed_vat_rates:
            raise ValueError(f'Недопустимый НДС: {vat_rate}. Допустимо: {allowed_vat_rates}')

        if amount_without_vat is None:
            amount_without_vat = round(random.uniform(100.0, 1_000_000.0), 2)
        else:
            amount_without_vat = round(amount_without_vat, 2)

        vat_amount = round(amount_without_vat * vat_rate / 100, 2)
        total_amount = round(amount_without_vat + vat_amount, 2)

        return ActData(
            amount_without_vat=amount_without_vat,
            vat_rate=vat_rate,
            vat_amount=vat_amount,
            total_amount=total_amount,
        )

    @staticmethod
    def generate_username(length: int = 10) -> str:
        """
        Генерирует случайный username (буквы + цифры).
        Максимальная длина — 15 символов.

        Args:
            length: Длина username (по умолчанию 10, макс. 15)

        Returns:
            str: Сгенерированный username

        >>> DataHelper.generate_username(8)
        'user_a3k9'  # пример
        """
        length = min(length, 15)  # ограничиваем макс. длину
        prefix = 'user_'
        random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length - len(prefix)))
        return f'{prefix}{random_part}'

    @staticmethod
    def generate_email(domain: str = 'testmail.com', prefix: str = None) -> str:
        """
        Генерирует валидный email для тестов.

        Args:
            domain: Домен почтового ящика (по умолчанию 'testmail.com')
            prefix: Префикс email (по умолчанию генерируется случайно)

        Returns:
            str: Сгенерированный email

        >>> DataHelper.generate_email()
        'test_a3k9@ytestmail.com'  # пример
        >>> DataHelper.generate_email(domain='example.org')
        'test_b7x2@example.org'  # пример
        """
        if prefix is None:
            prefix = f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=4))}"
        return f'{prefix}@{domain}'

    @staticmethod
    def generate_password(length: int = 12,
                          use_special: bool = True,
                          max_length: int = 20) -> str:
        """
        Генерирует случайный пароль с буквами, цифрами и спецсимволами.

        Args:
            length: Длина пароля (по умолчанию 12)
            use_special: Использовать ли спецсимволы (!@#$%)
            max_length: Максимальная длина пароля (по умолчанию 20)

        Returns:
            str: Сгенерированный пароль

        >>> DataHelper.generate_password(10)
        'aB3$kL9@mN2'  # пример
        >>> DataHelper.generate_password(8, use_special=False)
        'aB3kL9mN'  # пример
        """
        length = min(length, max_length)  # ограничиваем макс. длину

        # Обязательные символы для надежности
        chars = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits)
        ]

        # Набор символов для заполнения
        all_chars = string.ascii_letters + string.digits
        if use_special:
            chars.append(random.choice('!@#$%'))
            all_chars += '!@#$%'

        # Заполняем остаток длины случайными символами
        chars += random.choices(all_chars, k=length - len(chars))

        # Перемешиваем и возвращаем
        random.shuffle(chars)
        return ''.join(chars)

    @staticmethod
    def generate_unique_prefix() -> str:
        """
        Генерирует уникальный префикс на основе timestamp.
        Полезно для предотвращения конфликтов данных в тестах.

        Returns:
            str: Уникальный префикс

        >>> DataHelper.generate_unique_prefix()
        '20250115_143022'  # пример
        """
        return datetime.now().strftime('%Y%m%d_%H%M%S')

data_helper = DataHelper()
