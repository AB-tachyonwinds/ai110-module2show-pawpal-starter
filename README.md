# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
Daily plan for Biscuit (Golden Retriever):
08:00 — Morning walk (30 min) [priority: high]
09:00 — Feeding (10 min) [priority: high]

Daily plan for Whiskers (Tabby):
09:30 — Litter box cleaning (15 min) [priority: low]

Total scheduled time: 55 minutes
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
python -m pytest

# Run with coverage:
pytest --cov
```

The tests cover basic app functionality (adding a task), recurrence for tasks, sorting lists, scheduling and conflicts, and edge cases like removing a nonexistent task.
Confidence level: 4

Sample test output:

```
============================================ test session starts =============================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0
rootdir: [your rootdir]
plugins: anyio-4.14.1
collected 21 items                                                                                            

tests\test_pawpal.py .....................                                                              [100%]

============================================= 21 passed in 0.06s =============================================
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_priority`, `Scheduler.sort_by_time` | Sorts tasks highest-to-lowest priority, or chronologically by `scheduled_time` (`HH:MM`) for display in the daily plan |
| Filtering | `Scheduler.generate_schedule`, `Pet.filter_tasks_by_completion` | Selects only a pet's incomplete tasks whose `due_date` matches the schedule date; owner-wide view aggregated in `generate_schedule_for_owner` |
| Conflict handling | `Scheduler.detect_conflicts` | Groups scheduled tasks by `scheduled_time` and emits a warning for any time slot shared by 2+ tasks (across pets) |
| Recurring tasks | `Task.create_next_occurrence`, `Pet.complete_task` | On completion, `daily`/`weekly` tasks (via `RECURRENCE_INTERVALS`) spawn a new incomplete `Task` with `due_date` advanced by the recurrence interval |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. Enter a name for the owner, then fill in the pet's name, species, breed, and age, and click **Add pet**.
2. Select the pet from the **Pet** dropdown (if there is more than one).
3. Fill in a task's title, duration (in minutes), and priority (low/medium/high), then set its due date and scheduled time (`HH:MM`). Click **Add task**.
4. Pick a **Schedule date** and click **Generate schedule**.
5. Review the results: total planned time for the day, any scheduling-conflict warnings for tasks sharing the same time slot, and each pet's daily plan sorted chronologically with task name, duration, and priority.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
