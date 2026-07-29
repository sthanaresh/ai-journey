This repository contains my practice projects and exercises while learning Python and working toward becoming an AI Engineer.

## Project: Prompt Template Manager

The `PromptTemplateManager` is a simple Python class that manages text templates containing variables enclosed in curly braces (`{}`).

It can:

* Render templates using provided values
* Detect missing template variables
* Display a readable object representation
* Extract all variable names from a template using regular expressions

---

## Features

### 1. Render Templates

Replace variables with actual values.

Example template:

```text
Hello {name}, you are {age} years old
```

Example output:

```text
Hello Naresh, you are 25 years old
```

---

### 2. Missing Variable Detection

If a required variable is not provided, the program returns a helpful error message instead of crashing.

Example:

```python
pt.render(name="Naresh")
```

Output:

```text
Error: Missing template variable: 'age'
```

---

### 3. List Template Variables

Extract all variable names from the template.

Example:

```python
pt.list_variables()
```

Output:

```python
['name', 'age']
```

---

### 4. Object Representation

Provides a readable representation of the object for debugging purposes using `__repr__()`.

Example:

```python
print(pt)
```

Output:

```text
PromptTemplateManager(template='Hello {name}, you are {age} years old')
```

---

## Technologies Used

* Python 3
* Regular Expressions (`re`)
* Classes and Objects
* Type Hints
* Exception Handling
* String Formatting

---

## Project Structure

```text
ai-engineer-journey/
│
├── prompt_template_manager.py
└── README.md
```

---

## Code Example

```python
import re


class PromptTemplateManager:
    def __init__(self, template: str):
        self.template = template

    def render(self, **kwargs) -> str:
        try:
            return self.template.format(**kwargs)
        except KeyError as e:
            return f"Error: Missing template variable: {e}"

    def __repr__(self):
        return f"PromptTemplateManager(template={self.template!r})"

    def list_variables(self) -> list[str]:
        return re.findall(r"\{(.*?)\}", self.template)
```

---

## Example Usage

```python
pt = PromptTemplateManager(
    "Hello {name}, you are {age} years old"
)

print(pt.render(name="Naresh", age=25))
print(pt.render(name="Naresh"))
print(pt)
print(pt.list_variables())
```

Expected output:

```text
Hello Naresh, you are 25 years old
Error: Missing template variable: 'age'
PromptTemplateManager(template='Hello {name}, you are {age} years old')
['name', 'age']
```

---

## Concepts Practiced

This project helped me practice:

* Python Classes
* Constructors (`__init__`)
* Dunder Methods (`__repr__`)
* Dictionaries
* Exception Handling (`try`, `except`)
* Type Hints
* Regular Expressions (`re`)
* String Formatting (`format`)
* Object-Oriented Programming (OOP)

---

## Learning Goal

This project is part of my journey toward becoming an AI Engineer. The goal is to build strong Python fundamentals before moving on to:

* FastAPI
* Machine Learning
* LLM Applications
* Retrieval-Augmented Generation (RAG)
* AI Agents
* Production AI Systems

---

Created as part of my AI Engineering learning journey.
