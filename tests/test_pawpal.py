from datetime import date

from pawpal_system import Pet, Task


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
