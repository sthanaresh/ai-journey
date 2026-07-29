# Let's build something you'll actually reuse: a simplified PromptTemplateManager — a class pattern used in real LLM apps (LangChain's PromptTemplate is basically this, dressed up).
# Requirements:
# pythonclass PromptTemplateManager:
#     def __init__(self, template: str):
#         # store the template, e.g. "Hello {name}, you are {age} years old"
#         ...

#     def render(self, **kwargs) -> str:
#         # fill in the template with kwargs
#         # should raise a KeyError-friendly message if a variable is missing
#         ...

#     def __repr__(self) -> str:
#         # nice debug view
#         ...
# Usage should work like this:
# pythonpt = PromptTemplateManager("Hello {name}, you are {age} years old")
# print(pt.render(name="Naresh", age=25))
# # → "Hello Naresh, you are 25 years old"

# print(pt.render(name="Naresh"))
# # → should NOT crash ugly; should catch the missing key and print something like:
# # "Error: Missing template variable: 'age'"
# Hint (only if stuck): Python strings have a built-in .format(**kwargs) method that does exactly the substitution — you just need to wrap it in try/except KeyError.
# Add a method list_variables(self) -> list[str] that returns all {variable} names
# found in the template (hint: look into the re module, or string parsing)

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
        return f"PromptTemplateManager(template = {self.template!r})"

    def list_variables(self) -> list[str]:
        return re.findall(r"\{(.*?)\}", self.template)


pt = PromptTemplateManager("Hello {name}, you are {age} years old")
print(pt.render(name="Naresh", age=25))
print(pt.render(name="Naresh"))
print(pt)  # This is the work of __repr__
print(pt.list_variables())
print("printing next run.................................")
