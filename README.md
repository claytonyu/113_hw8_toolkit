# 15-113 HW8 - Build Your Own Agent Toolkit
This repository was created for Homework 8 of 15-113, an Effective Coding with AI Course at CMU. 
I've confirmed that the tools work with Codex, and installation should be smoother with it.


## Skill: `check-code-style`
I've needed to repeatedly tell LLMs to write code with good style. For my [skill](.agents/skills/check-code-style/SKILL.md), I've written a checker that evaluates written code for good coding style.
Attribution: The first three core principles in the skill are a direct copy from one of my HW4 prompts for good coding principles, which come from a blog online (that I've lost the link to).

### Example of Writing Code with Good Style
**Prompt from HW4**
> You are a senior software architect. Strictly adhere to these principles:
> 1. KISS (Keep It Simple, Stupid): Write straightforward, uncomplicated logic. Avoid premature optimizations or speculative "what-if" abstractions.
> 2. YAGNI (You Aren't Gonna Need It): Do not add extra features, utility methods, or error-handling blocks for scenarios that cannot physically happen in this scope.
> 3. SOLID: Ensure conceptual single responsibility per class/function.
> 4. Reduce cognitive complexity (aim for low cyclomatic complexity).

**Prompt from HW6**:
> Can you also make your code more modular?
> 
> Also refactor the code to follow good coding practices (e.g. KISS)

### Skill Installation Instructions
Codex automatically finds the skill in `.agents/skills/*`. If using Claude, this skill would need to be moved to a `.claude/skills/` folder.


## MCP: `15-113 Assignment Reader`
Manually checking through the 15-113 assignment specification to see if I've finished everything is error-prone, so I created an MCP that loads the assignment pages from the course website (thanks for making the URLs consistent!)

### Example of Following Assignment Specification
I don't have an explicit call that asks AI to check assignment specifications, but many of my prompts are direct quotes from the webpage. For example, for HW7 (Code Handoff), we were asked not to significantly modify the existing code we were given.

**Prompt from HW7**:
> Refactor the code -- **do NOT overhaul or completely change it**. You may split & rename functions or files for modularity. Most of the work should be recognizable to the original code. Use the following principles: ...

### MCP Installation Instructions
#### Venv Installation
The MCP is in the [mcp](mcp) folder, and it requires packages listed in a requirements file. Run these commands to install a venv with Python/pip:
```bash
python -m venv mcp/.venv
mcp/.venv/bin/python -m pip install -r mcp/requirements.txt
```
Run this command to install it with uv:
```bash
uv venv mcp/.venv
uv pip install --python mcp/.venv/bin/python -r mcp/requirements.txt
```
This was tested on Python 3.14, but it should run with modern versions of Python.

#### MCP Installation
I decided to install the MCP locally in this project. Codex allows for project-level registration using the [.codex/config.toml](.codex/config.toml) file, and relative paths are allowed in this case.
I'm not sure how to install it with Claude, but the command to run the server would be `./mcp/.venv/bin/python ./mcp/assignment_reader_113.py`, with absolute paths filled in

## AI Usage
Codex with GPT-6.1 Terra was used for this project to run the skills/MCP to create the directories [run1-api](run1-api) and [run2-proj2](run2-proj2). AI responses from Claude may be found in [old_prompt_logs](old_prompt_logs). Codex was also used to troubleshoot installation issues for the MCP.
Everything else -- the top-level .md files, the shell excerpts above, the skills, the MCP code -- were written by me, except for the first three "core coding principles" in my skills. Help from online documentation was used to write these, of course.
The installation should be smoother with Codex compared to another agentic tool.