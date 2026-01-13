"""Модуль управления данными преподавателей."""


class Teacher:
    """Класс преподавателя."""

    def __init__(self, name, department):
        """ вносит данные о преподавателе """
        self.__name = name
        self.__department = department

    def assign_to_event(self, event):
        """Связывает преподавателя с конкретным событием."""
        event.teacher = self
        print(f"Преподаватель {self.__name} назначен на предмет {event.subject}")

if __name__ == '__main__':
    ...
    



