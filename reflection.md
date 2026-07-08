# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
Using Owner, Pet, Task, and Scheduler, we created a fairly minimal design for a pet scheduling app. Owners can have many pets and Pets can have many tasks. A scheduler can have many tasks.
- What classes did you include, and what responsibilities did you assign to each?
I only included the main 4 classes that are required. An owner has their information and the pet attached to them. The pets will have tasks attached to them that can be used to create a schedule based off the pet chosen.

**b. Design changes**

- Did your design change during implementation?
It changed a bit during implementation while looking for bottlenecks.
- If yes, describe at least one change and why you made it.
The AI suggestioned that the current design lacked back-references and shortcuts. We added pet and owner attributes to task and scheduler respectively for potential flexibility in the future. We also covered future bottlenecks such has a task having no due-date, which would prevent the scheduler's schedule_date from having a date to reference.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
