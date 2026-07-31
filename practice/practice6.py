class Cache:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.store = {}

    def add(self, key: str, value: str) -> None:
        if len(self.store) >= self.max_size:
            print("Cache full, cannot add")
            return
        self.store[key] = value

    def get(self, key: str) -> str:
        try:
            return self.store[key]
        except KeyError as e:
            return f"Key not found: {e}"


cache = Cache(2)
cache.add("a", "1")
cache.add("b", "2")
cache.add("c", "3")

print(cache.get("a"))
print(cache.get("c"))
