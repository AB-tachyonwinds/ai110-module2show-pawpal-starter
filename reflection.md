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
The constraints considered are due date, completition status, priority, and scheduled time. Duration is tracked by not enforced currently.

- How did you decide which constraints mattered most?
I tried to decide it based on what I imagined a pet owner would want. Some constraints are treated more importantly than others, such as the due date.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
My scheduler has exact time-match conflicts, but does not check for overlap.
- Why is that tradeoff reasonable for this scenario?
Exact time conflict is simpler to implement, which is better for the app's performance. For pet owners, many tasks are shorter and the exact time conflict will help catch accidents.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
I used Claude Code for much of the implementation. It helped me brainstorm and design many of the algorithms used. It also assisted in debugging and integrating the functionality between files. Many times, it would bring up a possible optimization or functionality in python that I wasn't aware about. I would accept it if I understood what it was writing.
- What kinds of prompts or questions were most helpful?
Prompts that were focused on one task were the most helpful. Spreading the AI too thinly.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
In one moment, the AI suggested getting rid of two functions that handled sorting (one for priority and one for time). For the sake of the project, we technically only needed to do one of them, but I did not accept the AI's suggestion to get rid of it because I wanted to keep it in case we wanted to add a toggle that sorted the list based on what the user sets. While in its current form, it might not be the best for our simple implementation but it could be useful for the future.
- How did you evaluate or verify what the AI suggested?
I evaluated what I wanted the app to have and what it would impact on the code if I didn't follow the suggestion.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
We tested happy cases, specific functionalities (like if a recurring task would reappear), and defensive edge cases (like trying to get rid of a task that doesn't exist).
- Why were these tests important?
These tests cover behaviors that users can potentially run into during normal use. 

**b. Confidence**

- How confident are you that your scheduler works correctly?
I am 80% confident that the scheduler works correctly. While I think much of the logic and implementation makes sense, I feel that my involvement was less present in this project.
- What edge cases would you test next if you had more time?
I would test when pets have the same data or adding many instances of conflicting data.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I am the most satisfied with the testing process. I felt we covered the needed bases for the scope of the project.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
I would simplify the attributes needed for the app and simplify functionality in general. While they can be used for future functions, I felt that many suggestions I allowed at the beginning made it more difficult for me to follow along and untangle in the later stages. Key design choices ended up not being made by me and moreso by the AI. While AI can provide certain insights, the lack of control makes me uncertain on the app's structural integrity.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
If I had one important takeaway, it's definitely be more prepared at the beginning with what you want to create for a system. Oftentimes, the initial draft can give you an idea and good starting point, but it should be considered with more scrutiny especially while working with AI.
