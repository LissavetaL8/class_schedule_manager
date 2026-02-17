"""Модуль для управления отдельными событиями расписания."""
from datetime import datetime

class Event:
  """Класс, описывающий учебное событие (лекцию, семинар и т.д.)."""
    
  def __init__(self, date_str: str, time_str: str, subject: str, location: str):
    """
        Базовый конструктор класса.
        :param date_str: Дата в формате ГГГГ-ММ-ДД.
        :param time_str: Время в формате ЧЧ:ММ.
        :param subject: Название предмета.
        :param location: Место проведения.
        """
    self.__dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    self.__subject = subject
    self.__location = location
    self.__teacher = None
      
  def get_dt(self) -> datetime:
    """Возвращает дату и время события."""
    return self.__dt
      
  def get_subject(self) -> str:
    """Возвращает название предмета."""
    return self.__subject
      
  def get_location(self) -> str:
    """Возвращает место проведения."""
    return self.__location
      
  def get_teacher(self):
    """Возвращает объект преподавателя, назначенного на событие."""
    return self.__teacher
      
  def set_dt(self, dt_str: str, time_str: str):
    """
        Устанавливает новую дату и время события.
        :param dt_str: Новая дата в формате ГГГГ-ММ-ДД.
        :param time_str: Новое время в формате ЧЧ:ММ.
        """
    self.__dt = datetime.strptime(f"{dt_str} {time_str}", "%Y-%m-%d %H:%M")
      
  def set_subject(self, subject: str):
    """
        Устанавливает новое название предмета.
        :param subject: Новое название предмета.
        """
    self.__subject = subject
      
  def set_location(self, location: str):
    """
        Устанавливает новое место проведения.
        :param location: Новое место проведения.
        """
    self.__location = location
      
  def set_teacher(self, teacher):
    """
        Назначает преподавателя на событие.
        :param teacher: Объект преподавателя.
        """
    if not isinstance(teacher, Teacher):
      raise TypeError("Аргумент 'teacher' должен быть экземпляром класса Teacher.")
    self.__teacher = teacher
      
  def __repr__(self):
    """
        Возвращает строковое представление объекта Event.
        """
    t_name = self.__teacher.get_name() if self.__teacher else "Не назначен"
    return (
        f"[{self.__dt.strftime('%d.%m %H:%M')}] {self.__subject} ({self.__location}) | "
        f"Преподаватель: {t_name}"
    )
      
if __name__ == '__main__':
    ...
    








