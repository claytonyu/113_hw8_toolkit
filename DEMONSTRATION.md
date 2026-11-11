# Two Demonstrations of MCP + Skill Runs
Since my skill was to check if code was written with good style, the first agent must create code somehow with my MCP. The cleanest demonstration (though contrived) was to ask the model to generate code for two 15-113 assignments in two scenarios.

## Reflections
The checker caught the poor-readability of certain bits of code (ex: line 26 of [run1-api/iss.py](run1-api/iss.py)), and mainly the lack of docstring items. However, it also listed issues with functionality, which wasn't the goal of this skill, though appreciated. I would probably fine-tune it in the future to focus on readability and modularity.
It didn't list any necessary major structural changes to the code, which I agree with. Since I asked the agent to generate a 'minimal' model, there are no structural changes to make.


## Run 1 - API

### Creator Agent
I asked Codex to find a complete the coding portion of "a 15-113 assignment that had to do with APIs." Note that it searched multiple homework pages to find the right assignment.

> **Prompt**: Find a 15-113 assignment that had to do with APIs. Write a very minimal but complete assignment that satisfies the coding portion, using satellite APIs. Do ALL of your work in a folder called run1-api
> 
> **Response**: I’ll find the relevant 15-113 assignment and its coding requirements, then build a minimal satellite API project in run1-api.
> 
> `(Get Homework Page [9 calls])`
> 
> HW3, “Explore an API,” fits: it asks for a small app that fetches changing public API data, with useful handling for bad input and failed requests. I’ll make a small interactive ISS tracker and document how to run it.
>
> `(Ran commands, searched the web)`
> 
> Built a minimal interactive ISS tracker for 15-113 HW3: Explore an API in [run1-api](run1-api). It fetches the station’s position and calculates its approximate surface distance from coordinates the user enters.
> Run it with python3 run1-api/iss.py. The [README](run1-api/README.md) includes setup and API details.

### Checker Agent
In a separate window, I verified the code for readability & good coding practices.
> **Prompt**: Check the .py file in run1-api
> 
> **Response**: I’ll check the Python file for correctness and readability, then report any issues I find.
> 
> `(Read Check Code Style skill)`
> 
> [iss.py](run1-api/iss.py)
> - Line 11: coordinates lacks a docstring and type hints; its name could also make clearer that it parses input.
> - ... // Cut for brevity
> - Line 41: The broad exception handler reports all failures as connection problems, including malformed API data. That can make the actual cause difficult to diagnose.
> - Line 45: main lacks a docstring and return type hint.
> The coordinate parser and a sample distance calculation worked in a local check. I did not test a live API request.

## Run 2 - Project 2 (Database) Remake

### Creator Agent
> **Prompt**: I want to make a sample project 2 for 15-113. Write some code that mimics a front-end and back-end that could be fleshed out to finish project 2. Make the back-end functional. Make it very minimal; you don't need to link them up. Do ALL of your work in a folder called run2-proj2
>
> **Response**: I’ll check the Project 2 requirements and the existing workspace first, then build a minimal frontend and functional backend in run2-proj2.
>
> `(Get Project Page & other commands)`
>
> Project 2 is an open-ended creative web app. I’ll use a small “idea garden” as the example: a static interface mockup and a separate Python API that saves ideas in SQLite.
> ... // Cut for brevity
> Created [run2-proj2](run2-proj2), a minimal “Idea Garden” starter with a static frontend preview and a separate Python API that saves ideas in SQLite.

### Checker Agent
I typed an intentionally vague statement to see if the skill would activate. It did!

> **Prompt**: Evaluate the run2-proj2 code.
>
> **Response**: I’ll review the project’s code for correctness and readability, then report the most important findings with file references. I’ll use the check-code-style skill to guide the review.
>
> `(Read Check Code Style skill, listed files)`
>
> [server.py](run2-proj2/backend/server.py)
> - Line 13: connect() and the other functions and methods lack return and parameter type hints, as well as brief descriptions of their purposes.
> - Line 20: The SQLite connection context manager commits or rolls back transactions but does not close the connection. Explicitly close connections after each request to avoid relying on garbage collection.
> - ... // Cut for brevity
> - Line 64: The long route and ID validation condition is difficult to scan; a named helper or separate checks would clarify it.
> 
> [index.html](run2-proj2/frontend/index.html)
> - Line 1: The file lacks a brief comment describing its role as a static preview.
> - Line 8: Putting each CSS rule on one line makes individual properties harder to scan and change.
> The frontend is intentionally a disabled preview, as its README states, so it cannot yet create or display saved ideas. This was a read-only review; I did not run the application or tests.