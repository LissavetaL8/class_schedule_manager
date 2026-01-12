"""Модуль управления данными преподавателей."""


class Teacher:
    """Класс преподавателя."""

    def __init__(self, name, department):
        self.name = name
        self.department = department

    def assign_to_event(self, event):
        """Связывает преподавателя с конкретным событием."""
        event.teacher = self
        print(f"Преподаватель {self.name} назначен на предмет {event.subject}")

if __name__ == '__main__':
    ...
    
