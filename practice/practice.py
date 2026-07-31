class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name

        self.salary = salary


b = Employee("Naresh", "4000")
print(b.salary)


