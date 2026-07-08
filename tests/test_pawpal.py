from datetime import date

from pawpal_system import Owner, Pet, Scheduler, Task


def make_task(**overrides):
    defaults = dict(
        task_id="t1",
        name="Feed",
        description="Feed the pet",
        duration=10,
        priority=1,
        due_date=date(2026, 7, 7),
        pet_id="p1",
    )
    defaults.update(overrides)
    return Task(**defaults)


def test_mark_complete_changes_status():
    task = Task(
        task_id="t1",
        name="Feed",
        description="Feed the pet",
        duration=10,
        priority=1,
        due_date=date(2026, 7, 7),
        pet_id="p1",
    )
    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_add_task_increases_pet_task_count():
    pet = Pet(pet_id="p1", name="Rex", species="Dog", breed="Lab", age=3)
    task = Task(
        task_id="t1",
        name="Walk",
        description="Walk the pet",
        duration=20,
        priority=2,
        due_date=date(2026, 7, 7),
        pet_id="",
    )
    assert len(pet.get_tasks()) == 0

    pet.add_task(task)

    assert len(pet.get_tasks()) == 1


# --- Recurrence ---


def test_create_next_occurrence_returns_none_when_not_recurring():
    task = make_task(recurrence=None)

    assert task.create_next_occurrence() is None


def test_create_next_occurrence_returns_none_for_unknown_recurrence():
    task = make_task(recurrence="monthly")

    assert task.create_next_occurrence() is None


def test_create_next_occurrence_advances_due_date_daily():
    task = make_task(recurrence="daily", due_date=date(2026, 7, 7))

    next_task = task.create_next_occurrence()

    assert next_task is not None
    assert next_task.due_date == date(2026, 7, 8)
    assert next_task.completed is False


def test_create_next_occurrence_advances_due_date_weekly_across_month_boundary():
    task = make_task(recurrence="weekly", due_date=date(2026, 7, 28))

    next_task = task.create_next_occurrence()

    assert next_task.due_date == date(2026, 8, 4)


def test_complete_task_adds_next_occurrence_when_recurring():
    pet = Pet(pet_id="p1", name="Rex", species="Dog", breed="Lab", age=3)
    pet.add_task(make_task(task_id="t1", recurrence="daily"))

    pet.complete_task("t1")

    assert len(pet.get_tasks()) == 2
    original = next(t for t in pet.get_tasks() if t.task_id == "t1")
    assert original.completed is True
    new_tasks = [t for t in pet.get_tasks() if t.task_id != "t1"]
    assert len(new_tasks) == 1
    assert new_tasks[0].completed is False


def test_complete_task_does_not_add_occurrence_when_not_recurring():
    pet = Pet(pet_id="p1", name="Rex", species="Dog", breed="Lab", age=3)
    pet.add_task(make_task(task_id="t1", recurrence=None))

    pet.complete_task("t1")

    assert len(pet.get_tasks()) == 1


def test_complete_task_with_unknown_id_does_nothing():
    pet = Pet(pet_id="p1", name="Rex", species="Dog", breed="Lab", age=3)
    pet.add_task(make_task(task_id="t1"))

    pet.complete_task("does-not-exist")

    assert len(pet.get_tasks()) == 1
    assert pet.get_tasks()[0].completed is False


# --- Sorting ---


def test_sort_by_priority_empty_list_returns_empty():
    owner = Owner(owner_id="o1", name="Ann", email="a@example.com", phone="555")
    scheduler = Scheduler(schedule_date=date(2026, 7, 7), owner=owner)

    assert scheduler.sort_by_priority([]) == []


def test_sort_by_priority_orders_high_to_low():
    owner = Owner(owner_id="o1", name="Ann", email="a@example.com", phone="555")
    scheduler = Scheduler(schedule_date=date(2026, 7, 7), owner=owner)
    low = make_task(task_id="low", priority=1)
    high = make_task(task_id="high", priority=3)
    medium = make_task(task_id="medium", priority=2)

    result = scheduler.sort_by_priority([low, high, medium])

    assert [task.task_id for task in result] == ["high", "medium", "low"]


def test_priority_label_unknown_for_out_of_range_priority():
    task = make_task(priority=0)

    assert task.priority_label == "unknown"


def test_sort_by_time_orders_chronologically_across_double_digit_hours():
    owner = Owner(owner_id="o1", name="Ann", email="a@example.com", phone="555")
    scheduler = Scheduler(schedule_date=date(2026, 7, 7), owner=owner)
    nine = make_task(task_id="nine", scheduled_time="9:00")
    ten = make_task(task_id="ten", scheduled_time="10:00")

    result = scheduler.sort_by_time([ten, nine])

    assert [task.task_id for task in result] == ["nine", "ten"]


# --- Scheduling / conflicts ---


def test_generate_schedule_excludes_completed_and_other_dates():
    pet = Pet(pet_id="p1", name="Rex", species="Dog", breed="Lab", age=3)
    pet.add_task(make_task(task_id="due-today", due_date=date(2026, 7, 7)))
    pet.add_task(make_task(task_id="due-later", due_date=date(2026, 7, 8)))
    completed_today = make_task(task_id="completed-today", due_date=date(2026, 7, 7))
    completed_today.mark_complete()
    pet.add_task(completed_today)

    owner = Owner(owner_id="o1", name="Ann", email="a@example.com", phone="555")
    owner.add_pet(pet)
    scheduler = Scheduler(schedule_date=date(2026, 7, 7), owner=owner)

    result = scheduler.generate_schedule(pet)

    assert [task.task_id for task in result] == ["due-today"]


def test_generate_schedule_for_owner_with_no_pets_returns_empty():
    owner = Owner(owner_id="o1", name="Ann", email="a@example.com", phone="555")
    scheduler = Scheduler(schedule_date=date(2026, 7, 7), owner=owner)

    assert scheduler.generate_schedule_for_owner() == []


def test_detect_conflicts_flags_same_time_different_pets():
    pet1 = Pet(pet_id="p1", name="Rex", species="Dog", breed="Lab", age=3)
    pet2 = Pet(pet_id="p2", name="Milo", species="Cat", breed="Tabby", age=2)
    pet1.add_task(make_task(task_id="t1", pet_id="p1", scheduled_time="9:00"))
    pet2.add_task(make_task(task_id="t2", pet_id="p2", scheduled_time="9:00"))

    owner = Owner(owner_id="o1", name="Ann", email="a@example.com", phone="555")
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    scheduler = Scheduler(schedule_date=date(2026, 7, 7), owner=owner)

    warnings = scheduler.detect_conflicts()

    assert len(warnings) == 1
    assert "9:00" in warnings[0]


def test_detect_conflicts_no_warning_for_single_task_at_time():
    pet = Pet(pet_id="p1", name="Rex", species="Dog", breed="Lab", age=3)
    pet.add_task(make_task(task_id="t1", scheduled_time="9:00"))

    owner = Owner(owner_id="o1", name="Ann", email="a@example.com", phone="555")
    owner.add_pet(pet)
    scheduler = Scheduler(schedule_date=date(2026, 7, 7), owner=owner)

    assert scheduler.detect_conflicts() == []


def test_detect_conflicts_with_explicit_empty_list():
    owner = Owner(owner_id="o1", name="Ann", email="a@example.com", phone="555")
    scheduler = Scheduler(schedule_date=date(2026, 7, 7), owner=owner)

    assert scheduler.detect_conflicts(tasks=[]) == []


# --- Pet / Owner CRUD ---


def test_remove_task_with_unknown_id_leaves_tasks_unchanged():
    pet = Pet(pet_id="p1", name="Rex", species="Dog", breed="Lab", age=3)
    pet.add_task(make_task(task_id="t1"))

    pet.remove_task("does-not-exist")

    assert len(pet.get_tasks()) == 1


def test_remove_pet_with_unknown_id_leaves_pets_unchanged():
    owner = Owner(owner_id="o1", name="Ann", email="a@example.com", phone="555")
    owner.add_pet(Pet(pet_id="p1", name="Rex", species="Dog", breed="Lab", age=3))

    owner.remove_pet("does-not-exist")

    assert len(owner.get_pets()) == 1


def test_filter_tasks_by_completion_on_empty_pet():
    pet = Pet(pet_id="p1", name="Rex", species="Dog", breed="Lab", age=3)

    assert pet.filter_tasks_by_completion(True) == []
    assert pet.filter_tasks_by_completion(False) == []
