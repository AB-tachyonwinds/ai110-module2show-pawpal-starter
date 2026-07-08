from datetime import date

import streamlit as st
from pawpal_system import Owner, Pet, Scheduler, Task

PRIORITY_VALUES = {"low": 1, "medium": 2, "high": 3}

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
breed = st.text_input("Breed", value="Unknown")
age = st.number_input("Age", min_value=0, max_value=30, value=1)

if "owner" not in st.session_state:
    st.session_state.owner = Owner(owner_id="owner-1", name=owner_name, email="", phone="")

owner = st.session_state.owner

if st.button("Add pet"):
    pet_id = f"pet-{len(owner.get_pets()) + 1}"
    new_pet = Pet(pet_id=pet_id, name=pet_name, species=species, breed=breed, age=int(age))
    owner.add_pet(new_pet)

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

pets = owner.get_pets()
if not pets:
    st.info("No pets yet. Add one above.")
else:
    pet_names = [f"{p.name} ({p.pet_id})" for p in pets]
    selected_index = st.selectbox(
        "Pet", range(len(pets)), format_func=lambda i: pet_names[i]
    )
    selected_pet = pets[selected_index]

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

due_date = st.date_input("Due date", value=date.today())
scheduled_time = st.text_input("Scheduled time (HH:MM)", value="09:00")

if st.button("Add task"):
    task_id = f"task-{len(selected_pet.get_tasks()) + 1}"
    new_task = Task(
        task_id=task_id,
        name=task_title,
        description="",
        duration=int(duration),
        priority=PRIORITY_VALUES[priority],
        due_date=due_date,
        pet_id=selected_pet.pet_id,
        scheduled_time=scheduled_time,
    )
    selected_pet.add_task(new_task)

if selected_pet.get_tasks():
    st.write("Current tasks:")
    st.table(
        [
            {
                "title": t.name,
                "duration_minutes": t.duration,
                "priority": t.priority_label,
                "due_date": str(t.due_date),
                "scheduled_time": t.scheduled_time,
            }
            for t in selected_pet.get_tasks()
        ]
    )
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

schedule_date = st.date_input("Schedule date", value=date.today(), key="schedule_date")

if st.button("Generate schedule"):
    if not owner.get_pets():
        st.info("Add a pet and some tasks first.")
    else:
        scheduler = Scheduler(schedule_date=schedule_date, owner=owner)
        daily_tasks = scheduler.get_daily_schedule()
        if not daily_tasks:
            st.info("No tasks due on this date.")
        else:
            for pet in owner.get_pets():
                plan = scheduler.format_pet_daily_plan(pet)
                st.text(plan)

    #     st.warning(
#         "Not implemented yet. Next step: create your scheduling logic (classes/functions) and call it here."
#     )
#     st.markdown(
#         """
# Suggested approach:
# 1. Design your UML (draft).
# 2. Create class stubs (no logic).
# 3. Implement scheduling behavior.
# 4. Connect your scheduler here and display results.
# """
#     ) 
