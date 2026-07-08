from dataclasses import dataclass, field
from datetime import date


@dataclass
class Task:
    task_id: str
    name: str
    description: str
    duration: int
    priority: int
    completed: bool = False

    def edit_duration(self, minutes: int) -> None:
        pass

    def edit_priority(self, level: int) -> None:
        pass

    def mark_complete(self) -> None:
        pass

    def mark_incomplete(self) -> None:
        pass


@dataclass
class Pet:
    pet_id: str
    name: str
    species: str
    breed: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task_id: str) -> None:
        pass

    def get_tasks(self) -> list[Task]:
        pass

    def update_info(self, name: str, breed: str, age: int) -> None:
        pass


@dataclass
class Owner:
    owner_id: str
    name: str
    email: str
    phone: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, pet_id: str) -> None:
        pass

    def get_pets(self) -> list[Pet]:
        pass

    def update_contact_info(self, email: str, phone: str) -> None:
        pass


@dataclass
class Scheduler:
    schedule_date: date
    scheduled_tasks: list[Task] = field(default_factory=list)

    def generate_schedule(self, pet: Pet) -> list[Task]:
        pass

    def sort_by_priority(self, tasks: list[Task]) -> list[Task]:
        pass

    def calculate_total_duration(self, tasks: list[Task]) -> int:
        pass

    def get_daily_schedule(self) -> list[Task]:
        pass
