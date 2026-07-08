from dataclasses import dataclass, field
from datetime import date


PRIORITY_LABELS = {1: "low", 2: "medium", 3: "high"}


@dataclass
class Task:
    task_id: str
    name: str
    description: str
    duration: int
    priority: int
    due_date: date
    pet_id: str
    scheduled_time: str = "00:00"
    completed: bool = False

    def edit_duration(self, minutes: int) -> None:
        """Update the task's duration in minutes."""
        self.duration = minutes

    def edit_priority(self, level: int) -> None:
        """Update the task's priority level."""
        self.priority = level

    def edit_scheduled_time(self, scheduled_time: str) -> None:
        """Update the task's scheduled time."""
        self.scheduled_time = scheduled_time

    @property
    def priority_label(self) -> str:
        """Return the human-readable label for the task's priority."""
        return PRIORITY_LABELS.get(self.priority, "unknown")

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    def mark_incomplete(self) -> None:
        """Mark the task as not completed."""
        self.completed = False


@dataclass
class Pet:
    pet_id: str
    name: str
    species: str
    breed: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        task.pet_id = self.pet_id
        self.tasks.append(task)

    def remove_task(self, task_id: str) -> None:
        """Remove the task with the given ID from this pet's task list."""
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def get_tasks(self) -> list[Task]:
        """Return this pet's list of tasks."""
        return self.tasks

    def update_info(self, name: str, breed: str, age: int) -> None:
        """Update the pet's name, breed, and age."""
        self.name = name
        self.breed = breed
        self.age = age


@dataclass
class Owner:
    owner_id: str
    name: str
    email: str
    phone: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's list of pets."""
        self.pets.append(pet)

    def remove_pet(self, pet_id: str) -> None:
        """Remove the pet with the given ID from this owner's list of pets."""
        self.pets = [pet for pet in self.pets if pet.pet_id != pet_id]

    def get_pets(self) -> list[Pet]:
        """Return this owner's list of pets."""
        return self.pets

    def update_contact_info(self, email: str, phone: str) -> None:
        """Update the owner's email and phone number."""
        self.email = email
        self.phone = phone


@dataclass
class Scheduler:
    schedule_date: date
    owner: Owner
    scheduled_tasks: list[Task] = field(default_factory=list)

    def generate_schedule(self, pet: Pet) -> list[Task]:
        """Return the pet's incomplete tasks due on the schedule date."""
        return [
            task
            for task in pet.get_tasks()
            if task.due_date == self.schedule_date and not task.completed
        ]

    def generate_schedule_for_owner(self) -> list[Task]:
        """Return and cache the scheduled tasks across all of the owner's pets."""
        self.scheduled_tasks = []
        for pet in self.owner.pets:
            self.scheduled_tasks.extend(self.generate_schedule(pet))
        return self.scheduled_tasks

    def sort_by_priority(self, tasks: list[Task]) -> list[Task]:
        """Return the tasks sorted from highest to lowest priority."""
        return sorted(tasks, key=lambda task: task.priority, reverse=True)

    def calculate_total_duration(self, tasks: list[Task]) -> int:
        """Return the total duration in minutes for the given tasks."""
        return sum(task.duration for task in tasks)

    def get_daily_schedule(self) -> list[Task]:
        """Return the owner's scheduled tasks sorted by priority."""
        return self.sort_by_priority(self.generate_schedule_for_owner())

    def sort_by_time(self, tasks: list[Task]) -> list[Task]:
        """Return the tasks sorted by scheduled time."""
        return sorted(tasks, key=lambda task: task.scheduled_time)

    def format_pet_daily_plan(self, pet: Pet) -> str:
        """Return a formatted string of the pet's daily task plan."""
        tasks = self.sort_by_time(self.generate_schedule(pet))
        lines = [f"Daily plan for {pet.name} ({pet.breed}):"]
        for task in tasks:
            lines.append(
                f"{task.scheduled_time} — {task.name} ({task.duration} min) "
                f"[priority: {task.priority_label}]"
            )
        return "\n".join(lines)

    def print_daily_plan(self) -> None:
        """Print each pet's daily plan to stdout."""
        for pet in self.owner.pets:
            print(self.format_pet_daily_plan(pet))
            print()
