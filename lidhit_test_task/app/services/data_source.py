from abc import ABC, abstractmethod


class DataSource(ABC):
    """
    Абстрактный класс необходимый для нахождения названия шаблона формы.
    Будет являться родителем для потомков реализующие взаимодействия с различными источниками данных.
    """

    TMPL_DATE = 'date'
    TMPL_PHONE = 'phone'
    TMPL_EMAIL = 'email'
    TMPL_TEXT = 'text'

    @abstractmethod
    def get_form(self) -> str | dict:
        """
        Возвращает результат поиска в виде строки с именем шаблона
        или словаря приведеных типов
        :return: str | dict
        """
        pass

    @abstractmethod
    def _get_all_templates(self) -> iter:
        """
        Возвращает итератор с всеми шаблонами форм в БД
        :return: iter
        """
        pass

    def _convert_field_value(self) -> dict:
        """
        Метод проводит валидацию значений полей,
        и возвращает словарь в котором полю присваевается тип данных
        :return: dict
        """
        result = dict()
        for key, value in self.data.items():
            value = value.strip()
            if self.validate_date(value, '%Y-%m-%d') or self.validate_date(value, '%d.%m.%Y'):
                result[key] = type(self).TMPL_DATE
            elif self.validate_phone(value):
                result[key] = type(self).TMPL_PHONE
            elif self.validate_email(value):
                result[key] = type(self).TMPL_EMAIL
            else:
                result[key] = type(self).TMPL_TEXT

        return result
