# Exercise A: Create a class VectorStore with:

# __init__(self, name: str, dimension: int)
# A method add_vector(self, vector: list[float]) -> None
# that prints "Added vector of length {len(vector)} to {name}"
# A __repr__ that shows the name and dimension


class VectorStore:
    def __init__(self, name: str, dimension: int):
        self.name = name
        self.dimension = dimension

    def add_vector(self, vector: list[float]):
        print(f"Added vector of length{len(vector)} to {self.name}")

    def __repr__(self):
        return f"VectorStore (name={self.name}, dimension={self.dimension})"
