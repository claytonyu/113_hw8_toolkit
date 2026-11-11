---
name: check-code-style
description: Evaluate code for good style and readability. Use when asked to check over code, or as the first step when prompted to "refactor" code.
---

# Check Code Style
You will evaluate the project code of relevant scope for good style.
During the code check, never modify any of the files you read. This skill should be read-only.
For every file, evaluate for the following principles. Then flag any violations following the output format below.

## Core Principles
1. KISS (Keep It Simple, Stupid): Straightforward, uncomplicated logic. Prioritize plain, clear, idiomatic code over overly clever or compressed one-liners.
2. YAGNI (You Aren't Gonna Need It): Check for extra features, utility methods, or error-handling blocks for scenarios that cannot physically happen in this scope.
3. SRP (Single Responsibility Principle): Ensure conceptual single responsibility per class/function.
4. Modularity: If the codebase or a particular file is becoming large, ensure functionality is split into multiple files according to their purpose or function. This is less important for early prototyping or smaller projects. Also ensure files are not being unnecessarily split.
5. Descriptive Naming: Use clear, meaningful names for variables, functions, and classes. If in Python, use type hints.

## Commenting
1. Each function and class should have a brief and useful comment (according to the language's style conventions) describing its purpose and usage.
2. Each file should have a module-level comment. It should be descriptive enough for others to understand and use it.
3. Anything that is unintuitive or complex should have a comment.
4. Explain the why, not the what. Don't narrate what the code is literally doing.

# Output Format
Flag any violations of these principles in your output. They should have the format:
```
**filename1**
- Line N: violation description 1.
- Line M: violation description 2.

**filename2**
- Line O: violation description 1.
- Line P: violation description 2.
- Line Q: violation description 3.
```
Try to keep the violation description concise (one phrase or sentence), but it can go to 2-3 sentences maximum if needed.

Then, after all this, note any major structural changes that should be made, in a `Structural Changes` section, if any are needed. This can include bad code design of an entire class or system, merging / splitting files, etc.