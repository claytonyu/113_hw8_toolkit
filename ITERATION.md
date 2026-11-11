# Improving the `check-code-style` skill

## Before

My check-code-style skill was firing in places where I didn't want it to. The prompt "Check the .py file" fired the skill, which was not intended.

Original Description: `Evaluate code for good style and readability. Use when asked to check over code, or as the first step when prompted to "refactor" code.`

> **Prompt**: Check the .py file in run1-api
>
> **Response**: `Loaded the check-code-style` skill.

## After

Although this prompt is related to the skill, I realized I wanted the skill only to fire when explicitly asked about the "maintainability," "readability," or "style" of code. Now, "Check the .py file" no longer runs the check-code-style skill.

New Description: `Evaluate code for style, readability, and maintainability. Use when asked to review code specifically for these reasons, or as the first step when prompted to "refactor" code, but not when simply asked to summarize or view code.`

> **Prompt**: Check the .py file in run1-api
>
> **Response**: I checked [iss.py](iss.py). It fetches the ISS position and calculates its approximate surface distance from coordinates entered by the user...