from enum import StrEnum


class SelectCountry(StrEnum):
    """Страна в форме регистрации"""
    SELECT = "Select country..."
    RU = "Russia"
    US = "United States"
    UK = "United Kingdom"
    GE = "Germany"
