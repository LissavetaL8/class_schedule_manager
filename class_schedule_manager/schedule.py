"""Модуль управления расписанием."""
from datetime import timedelta, datetime

class Schedule:
  """Класс для хранения и обработки списка занятий."""
  def __init__(self):
    """
        Инициализирует расписание занятий.
        """
    self.__events = []  # список в котором будет храниться расписание занятий
      
  def add_event(self, event) -> bool:
    """
        Добавляет новое событие в расписание.
        :param event: Объект события, которое нужно добавить.
        :return: True, если событие успешно добавлено, False в противном случае.
        """
    if not isinstance(event, Event):
      raise TypeError("Аргумент 'event' должен быть экземпляром класса Event.")
    if self.check_conflict(event.get_dt()):
      print(f"Ошибка: Конфликт расписания на {event.get_dt()}")
      return False
        
    self.__events.append(event)
    self.__events.sort(key=lambda x: x.get_dt())
    return True
      
  def remove_event(self, subject: str, dt: datetime):
    """
        Удаляет занятие по названию и времени.
        :param subject: Название предмета, который нужно удалить.
        :param dt: Время события, которое нужно удалить.
        """
    self.__events = [
        e for e in self.__events if not (e.get_subject() == subject and e.get_dt() == dt)
    ]
      
  def check_conflict(self, dt: datetime) -> bool:
    """
        Проверяет, занято ли указанное время.
        :param dt: Время события для проверки.
        :return: True, если время занято другой дисциплиной, False, если указанный интервал времени свободен.
        """
    for e in self.__events:
      if abs(e.get_dt() - dt) < timedelta(hours=1, minutes=30):
        return True  # если время занято другой дисциплиной, в указанном интервале
    return False  # если время свободно
      
  def get_for_day(self, date_obj: datetime) -> list:
    """
        Возвращает события на конкретный день.
        :param date_obj: Дата, на которую нужно получить список пар.
        :return: Список объектов событий на заданный день.
        """
    return [e for e in self.__events if e.get_dt().date() == date_obj.date()]
      
  def show_all(self):
    """
        Печатает все расписание.
        """
    for e in self.__events:
      print(e)
  def get_events(self) -> list:
    """Возвращает список всех событий в расписании."""
    return self.__events
      
  def set_events(self, events: list):
    """
        Устанавливает новый список событий для расписания.
        :param events: Новый список событий.
        """
    if not all(isinstance(event, Event) for event in events):
      raise TypeError("Все элементы списка 'events' должны быть экземплярами класса Event.")
        
    self.__events = events
      
if __name__ == '__main__':
    ...
    






