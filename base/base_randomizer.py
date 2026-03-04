import random
import string
import time
from datetime import datetime
from typing import Any, Generator

from faker import Faker

garbage = '"¦O>”,“”‘~!@#$%^&*()?>,./<][/*<!–”\",“${code}”;–>\\"'
ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
cyrillic_letters = ru + RU


class BaseRandomizer:

    def __init__(self):
        self._faker = Faker('ru-RU')

    @staticmethod
    def unique_postfix() -> str:
        """Получить уникальный постфикс."""
        return str(time.time_ns())

    @staticmethod
    def get_current_timestamp() -> float:
        """Получить текущий timestamp."""
        return datetime.now().timestamp()

    def sentence(self, nb_words: int = 4) -> str:
        """Получить предложение из n-слов."""
        return self._faker.sentence(nb_words=nb_words)

    def large_text(self, max_nb_chars: int = 2000, use_line_break: bool = False) -> str:
        """Получить большой текст."""
        text = self._faker.text(max_nb_chars)
        if not use_line_break:
            text = text.replace('\r', '').replace('\n', '')
        return text

    @staticmethod
    def random_number(start: int = 1000, end: int = 9999999) -> int:
        """Получить случайное целое число."""
        return random.randint(start, end)

    @staticmethod
    def random_float_number(start: int | float = 1000, end: int | float = 9999999) -> float:
        """Получить случайное вещественное число."""
        return round(random.uniform(start, end), 3)

    def random_ru_string(self, char_count: int) -> str:
        """Получить случайный набор кириллических символов."""
        return self.random_id(length=char_count, is_latin=False, only_letters=True)

    def random_en_string(self, char_count: int) -> str:
        """Получить случайный набор латинских символов."""
        return self.random_id(length=char_count, is_latin=True, only_letters=True)

    @staticmethod
    def mix_string(value: str):
        """Перемешать строку."""
        list_of_char = list(value)
        random.shuffle(list_of_char)
        return ''.join(list_of_char)

    def random_id(
            self,
            length: int = 8,
            strong: bool = False,
            is_latin: bool = True,
            only_letters: bool = False,
            only_digits: bool = False,
            is_unique: bool = False
    ) -> str:
        """Получить случайный идентификатор, состоящий из цифр, букв или символов."""
        rid = ''
        for _ in range(length):
            rid += random.choice(
                self.mix_string(
                    ('!@#$%^&*()_-+=' if strong else '')
                    + ((string.ascii_letters if is_latin else cyrillic_letters) if not only_digits else '')
                    + (string.digits if not only_letters else '')
                )
            )
        if is_unique:
            rid = f'{rid}{self.unique_postfix()}'
        return rid

    def generate_name(self, mask: str) -> str:
        """Сгенерировать случайное имя с префиксом."""
        return '{mask}_{stamp}_{rand_id}'.format(mask=mask, stamp=int(datetime.now().timestamp()),
                                                 rand_id=self.random_id(length=6))

    def generate_unique_name_without_num(self, mask: str) -> str:
        """Сгенерировать случайное имя с префиксом без чисел."""
        return '{mask} {rand_id}'.format(mask=mask, rand_id=self.random_ru_string(15))

    def generate_unique_name_with_num(self, mask: str) -> str:
        """Сгенерировать уникальное имя с рандомным числом формата mask_000000000."""
        random_num = self.random_number(0, 999999999)  # от 0 до 999 999 999
        return '{mask}_{number:09d}'.format(mask=mask, number=random_num)

    def guid(self) -> str:
        return self._faker.uuid4()

    def md5(self) -> str:
        return self._faker.md5()

    @staticmethod
    def random_choice(array) -> Any:
        """Получить случайный элемент из списка."""
        return random.choice(array)

    @staticmethod
    def random_sample(array: list, n: int) -> list[Any]:
        """Получить случайный элемент из списка."""
        return random.sample(array, n)

    @staticmethod
    def random_choice_with_exclude(iterable, exclude=None) -> Any:
        """Получить случайный элемент из списка с возможностью задать список исключаемых элементов."""
        if not isinstance(exclude, list):
            exclude = [exclude]
        return random.choice([item for item in iterable if item not in exclude])

    @staticmethod
    def chunks(lst, n) -> Generator:
        """Yield successive n-sized chunks from list."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    @staticmethod
    def flatten_list(lst: list[list[Any]]) -> list[Any]:
        """Перевести вложенный список в прямой."""
        from itertools import chain

        return list(chain(*lst))

    @staticmethod
    def mix_list(lst: list[Any]) -> list[Any]:
        """Перемешивает список."""
        return sorted(lst, key=lambda x: random.random())

    def email(self) -> str:
        return self._faker.ascii_free_email()

    def unique_test_email(self, prefix: str = 'autotest') -> str:
        """Получить уникальное значение email."""
        return f'{prefix}_{self.unique_postfix()}@test.ru'

    def phone(self, mask: str = None) -> str:
        """Get random phone number.

        Return phone in random format or in format according to specified mask.
        :param mask: string in format like '+7(9xx)-xxx-xx-xx' where X will be replaced to random digit
        :return: random phone as string
        """
        if mask:
            return ''.join([(c, str(random.randint(0, 9)))[c == 'x'] for c in mask])
        return self._faker.phone_number()

    def url(self, schemes: list[str] | None = None) -> str:
        return self._faker.url(schemes)
