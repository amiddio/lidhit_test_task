import re

from datetime import datetime
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class ValidationMixin:
    """
    Статик методы для валидации различных типов данных
    """

    @staticmethod
    def validate_date(value: str, pattern: str) -> bool:
        """
        Валидация даты согласно паттерну
        :param value: str
        :param pattern: str
        :return: bool
        """
        try:
            datetime.strptime(value, pattern)
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_phone(value: str) -> bool:
        """
        Валидацие номера телефона.
        Валидными считаются такие например номера: '+7 123 456 78 90' или '+71234567890'
        :param value: str
        :return: bool
        """
        pattern = re.compile(r"^(\+7)\s?(\d{3})\s?(\d{3})\s?(\d{2})\s?(\d{2})$")
        match = re.search(pattern, value)
        if match:
            return True

        return False

    @staticmethod
    def validate_email(value: str) -> bool:
        """
        Валидация email-а на основе джанговской validate_email
        :param value: str
        :return: bool
        """
        try:
            validate_email(value)
            return True
        except ValidationError:
            return False
