from class_schedule_manager.event import Event
from class_schedule_manager.schedule import Schedule
from class_schedule_manager.teacher import Teacher


def main():
    print("=== Система управления расписанием 'UniSchedule' ===\n")

    # Создание расписания
    sched = Schedule()

    # Создание преподавателя
    teacher_ivanov = Teacher("Иванов И.И.", "Кафедра ИТ")

    # Добавление событий
    ev1 = Event("2026-01-20", "09:00", "Математика", "Ауд. 301")
    ev2 = Event("2026-01-20", "10:40", "Физика", "Ауд. 205")

    # Назначение преподавателя
    teacher_ivanov.assign_to_event(ev1)

    # Добавление событий в расписание
    sched.add_event(ev1)
    sched.add_event(ev2)

    # Проверка конфликта
    ev_bad = Event("2026-01-20", "09:15", "История", "Ауд. 101")
    sched.add_event(ev_bad)  # Должен вывести сообщение о конфликте

    print("\nТекущее расписание:")
    sched.show_all()


if __name__ == "__main__":
    main()
    





