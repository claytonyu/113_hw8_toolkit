# 15-113 HW8 - Build Your Own Agent Toolkit

I've needed to repeatedly tell LLMs to write code with good style. For my [skill](.agents/skills/check-code-style/SKILL.md), I've written a checker that evaluates written code for good style. The first couple of core principles are a direct copy from one of my HW4 prompts for good coding principles.
### Examples -- Writing Code with Good Style

**HW7**:
> Refactor the code -- do NOT overhaul or completely change it. You may split & rename functions or files for modularity. Most of the work should be recognizable to the original code. Use the following principles:
> 
> - KISS & Readability: Prioritize plain, clear, idiomatic code over overly clever or compressed one-liners
> - Modularity: In general, keep generated functions, classes, and modules focused on one specific job.
> - Add brief comments to each function describing its purpose, and a module-level comment per file. Comment anything that is unintuitive or complex.

**HW6**:
> Change the code to handle concurrently fetching arxiv and embedding, since it takes a lot of time.
> 
> Can you also make your code more modular?
> 
> Also refactor the code to follow good coding practices (e.g. KISS)