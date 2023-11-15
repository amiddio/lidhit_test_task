from typing import NoReturn

from django.conf import settings
from django.http import QueryDict
from tinydb import TinyDB

from .data_source import DataSource
from .validation_mixin import ValidationMixin


class TinydbDataSource(ValidationMixin, DataSource):
    """
    Класс использующий источник данных из TinyDB
    """

    def __init__(self, data: QueryDict) -> NoReturn:
        self.db = TinyDB(settings.DB_NAME)
        self.data = data

    def get_form(self) -> str | dict:
        converted_fields = self._convert_field_value()

        fields_from_request = (set(converted_fields.items()))
        for frm in self._get_all_templates():
            name = frm.pop('name')
            form_template = set(frm.items())
            if form_template.issubset(fields_from_request):
                return name

        return converted_fields

    def _get_all_templates(self):
        return iter(self.db)
