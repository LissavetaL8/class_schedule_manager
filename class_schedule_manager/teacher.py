"""Модуль управления данными преподавателей."""

class Teacher:
  """Класс для управления данными о преподавателе."""
  def __init__(self, name: str, department: str):
    """
        Инициализирует данные о преподавателе.
        :param name: ФИО преподавателя.
        :param department: Название кафедры или факультета.
        """
    self.__name = name
    self.__department = department
      
  @property
  def name(self) -> str:
    """
        Геттер для обращения к приватной переменной __name.
        Позволяет читать имя.
        :return: Значение приватного атрибута __name.
        """
    return self.__name
      
  def get_department(self) -> str:
    """Возвращает название кафедры/факультета."""
      
    return self.__department
      
  def set_name(self, name: str):
    """
        Устанавливает новое имя преподавателя.
        :param name: Новое имя.
        """
    self.__name = name
      
  def set_department(self, department: str):
    """
        Устанавливает новое название кафедры/факультета.
        :param department: Новое название кафедры/факультета.
        """
      
    self.__department = department
      
  def assign_to_event(self, event):
    """
        Связывает преподавателя с конкретным событием.
        :param event: Объект события/пары, к которому привязан преподаватель.
        """
    if not isinstance(event, Event):
      raise TypeError("Аргумент 'event' должен быть экземпляром класса Event.")
    event.set_teacher(self)
    print(f"Преподаватель {self.name} назначен на предмет {event.get_subject()}")
      
if __name__ == '__main__':
    






