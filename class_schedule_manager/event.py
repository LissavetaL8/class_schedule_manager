"""Модуль для управления отдельными событиями расписания."""
from datetime import datetime

class Event:
    """Класс, описывающий учебное событие (лекцию, семинар и т.д.)."""

    def __init__(self, date_str, time_str, subject, location):
        """
        :param date_str: Дата в формате ГГГГ-ММ-ДД
        :param time_str: Время в формате ЧЧ:ММ
        :param subject: Название предмета
        :param location: Место проведения
        retern: None
        """
        self.dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        self.subject = subject
        self.location = location
        self.teacher = None

    def __repr__(self):
        """ принимает данные о событие, возвращает текст, который включает дату, время, название предмета, место и имя преподавателя """
        t_name = self.teacher.name if self.teacher else "Не назначен"

        return f"[{self.dt.strftime('%d.%m %H:%M')}] {self.subject} ({self.location}) | Преподаватель: {t_name}"

if __name__ == '__main__':
    ...
    


