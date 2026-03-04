from enum import StrEnum


class UserRole(StrEnum):
    """Роли пользователей в системе"""
    SELECT = "-- Select --"
    ADMIN = "Admin"
    ESS = "ESS"
