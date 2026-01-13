from uni_schedule.event import Event
from uni_schedule.schedule import Schedule
from uni_schedule.teacher import Teacher


def main():
    print("=== Система управления расписанием 'UniSchedule' ===\n")

    sched = Schedule()
    teacher_ivanov = Teacher("Иванов И.И.", "Кафедра ИТ")

    # Добавление событий
    ev1 = Event("2026-01-20", "09:00", "Математика", "Ауд. 301")
    ev2 = Event("2026-01-20", "10:40", "Физика", "Ауд. 205")

    # Связка
    teacher_ivanov.assign_to_event(ev1)

    # Наполнение расписания
    sched.add_event(ev1)
    sched.add_event(ev2)

    # Проверка конфликта
    ev_bad = Event("2026-01-20", "09:15", "История", "Ауд. 101")
    sched.add_event(ev_bad)

    print("\nТекущее расписание:")
    sched.show_all()


if __name__ == "__main__":
    main()
    


