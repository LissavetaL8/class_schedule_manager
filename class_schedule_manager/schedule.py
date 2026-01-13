"""Модуль управления расписанием."""
from datetime import timedelta


class Schedule:
    """Класс для хранения и обработки списка занятий."""

    def __init__(self):
        """ принимает созданное расписание занятий
        :return: none """
        self._events = [] #список в котором будет храниться расписание занятий

    def add_event(self, event):
        
        """:event: объект, который нужно добавить в список
        :event.dt: Используется для проверки занятости времени
        :self._events: Список, в который добавляется новое событие"""
        
        if self.check_conflict(event.dt):
            print(f"Ошибка: Конфликт расписания на {event.dt}")
            return False
        self._events.append(event)
        self._events.sort(key=lambda x: x.dt)
        return True

    def remove_event(self, subject, dt):
        """Удаляет занятие по названию и времени
        принимает созданное расписание занятий, название предмета, который нужно удалить
        :return: none"""
        self._events = [e for e in self._events if not (e.subject == subject and e.dt == dt)]

    def check_conflict(self, dt):
        """Проверяет, занято ли указанное время
        принимает расписание и время события
        :return: bool"""
        
        for e in self._events:
            if abs(e.dt - dt) < timedelta(hours=1, minutes=30):
                return True #если время занято другой дисциплной, в указанном интервале
        return False #если время свободно

    def get_for_day(self, date_obj):
        """Возвращает события на конкретный день
        принимает рассписание и дату на которую нужно получить список пар
        :return: расписание пар на заданный день"""
        
        return [e for e in self._events if e.dt.date() == date_obj.date()]

    def show_all(self):
        """Печать всего расписания
        принимает созданное расписание 
        :return: полное расписание на весь период"""
        for e in self._events:
            print(e)

if __name__ == '__main__':
    ...
    



