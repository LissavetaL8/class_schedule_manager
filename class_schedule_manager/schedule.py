"""Модуль управления расписанием."""
from datetime import timedelta


class Schedule:
    """Класс для хранения и обработки списка событий."""

    def __init__(self):
        self._events = []

    def add_event(self, event):
        """Добавляет событие, проверяя на конфликты."""
        if self.check_conflict(event.dt):
            print(f"Ошибка: Конфликт расписания на {event.dt}")
            return False
        self._events.append(event)
        self._events.sort(key=lambda x: x.dt)
        return True

    def remove_event(self, subject, dt):
        """Удаляет событие по названию и времени."""
        self._events = [e for e in self._events if not (e.subject == subject and e.dt == dt)]

    def check_conflict(self, dt):
        """Проверяет, занято ли указанное время (упрощенно: окно в 1.5 часа)."""
        for e in self._events:
            if abs(e.dt - dt) < timedelta(hours=1, minutes=30):
                return True
        return False

    def get_for_day(self, date_obj):
        """Возвращает события на конкретный день."""
        return [e for e in self._events if e.dt.date() == date_obj.date()]

    def show_all(self):
        """Печать всего расписания."""
        for e in self._events:
            print(e)