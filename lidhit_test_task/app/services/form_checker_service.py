from typing import NoReturn

from .data_source import DataSource


class FormCheckerService:
    """
    Сервис являющийся посредником/слоем между представлением и данными
    """

    def __init__(self, data_source: DataSource) -> NoReturn:
        self.data_source = data_source

    def search(self) -> str | dict:
        """
        Метод ищет шаблон формы и возвращает название или словарь с приведением типов
        :return: str | dict
        """
        return self.data_source.get_form()
