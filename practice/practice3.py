# Exercise B: Create a class Agent that inherits from a base class BaseAgent:
# Make Agent override respond() to return f"{self.name} says: {message}".


class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    def respond(self, message: str) -> str:
        raise NotImplementedError


class Agent(BaseAgent):
    def respond(self, message: str) -> str:
        return f"{self.name} says:{message}"
