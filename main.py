import sys
from datetime import date

from pawpal_system import Owner, Pet, Task, Scheduler

sys.stdout.reconfigure(encoding="utf-8")

today = date(2026, 7, 7)

owner = Owner(owner_id="O1", name="John Doe", email="angelie@example.com", phone="555-0100")

dog = Pet(pet_id="P1", name="Biscuit", species="Dog", breed="Golden Retriever", age=3)
cat = Pet(pet_id="P2", name="Whiskers", species="Cat", breed="Tabby", age=2)

owner.add_pet(dog)
owner.add_pet(cat)

dog.add_task(Task(
    task_id="T1", name="Morning walk", description="Walk around the block",
    duration=30, priority=3, due_date=today, pet_id=dog.pet_id, scheduled_time="08:00",
))
dog.add_task(Task(
    task_id="T2", name="Feeding", description="Breakfast",
    duration=10, priority=3, due_date=today, pet_id=dog.pet_id, scheduled_time="09:00",
))
cat.add_task(Task(
    task_id="T3", name="Litter box cleaning", description="Clean the litter box",
    duration=15, priority=1, due_date=today, pet_id=cat.pet_id, scheduled_time="09:30",
))

scheduler = Scheduler(schedule_date=today, owner=owner)
scheduler.print_daily_plan()

total = scheduler.calculate_total_duration(scheduler.get_daily_schedule())
print(f"Total scheduled time: {total} minutes")
