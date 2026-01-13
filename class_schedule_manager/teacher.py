"""Модуль управления данными преподавателей."""


class Teacher:
    """Класс преподавателя."""

    def __init__(self, name, department):
        """ вносит данные о преподавателе 
        :name: ФИО преподавателя
        :department: название кафедры или факультета, на котором работает преподаватель
        :return: None"""
        
        self.__name = name
        self.__department = department

   @property
    def name(self):
        """ Геттер для обращения к приватной переменной __name.
        Позволяет читать имя, не изменяя его.
        :return: значение приватного атрибута __name """
        return self.__name
        
    def assign_to_event(self, event):
        """Связывает преподавателя с конкретным событием.
        :event: событие/пара к которому привязан преподаватель
        :return: имя преподавателя и предмет на который он назначен"""
        
        event.teacher = self
        print(f"Преподаватель {self.__name} назначен на предмет {event.subject}")

if __name__ == '__main__':
    ...
    


