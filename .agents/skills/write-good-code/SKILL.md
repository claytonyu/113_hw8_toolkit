---
name: write-good-code
description: Write code with good style, readability, and coding practices. Use when writing, refactoring, or adding features to code.
---

# Write Good Code

Writing human-readable and editable code that still performs its desired purpose.

## Core Principles
Follow style guidelines specific to the programming language you are working with. In addition, adhere strictly to these rules:
1. KISS (Keep It Simple, Stupid): Write straightforward, uncomplicated logic. Prioritize plain, clear, idiomatic code over overly clever or compressed one-liners.
2. YAGNI (You Aren't Gonna Need It): Do not add extra features, utility methods, or error-handling blocks for scenarios that cannot physically happen in this scope.
3. SRP (Single Responsibility Principle): Ensure conceptual single responsibility per class/function.
4. Reduce cognitive complexity (aim for low cyclomatic complexity).
5. Modularity: Split functionality into multiple files according to their purpose or function, especially if the codebase is becoming large. This is less important for early prototyping or smaller projects.
6. Descriptive Naming: Use clear, meaningful names for variables, functions, and classes.
7. Avoid Magic Numbers.

## Commenting
Good comments are the mark of a good programmer.
1. Add a brief comment at the top of each function and class (according to the language's style conventions) describing its purpose and usage.
2. Add a module-level comment per file. If the file documents a system of related functions, keep only the parts important for others to understand and use it.
3. Comment anything that is unintuitive or complex.
4. Explain the why, not the what. Don't narrate what the code is literally doing.

## After Completion
Unless otherwise told, output a brief and descriptive summary of what you have written. If any technical or design decisions were made, clearly list them.

## Specific Scenarios
- If you are asked to follow a SPEC.md, follow it! Ensure your code aligns with its requirements.
- If writing in Python, use type hints.