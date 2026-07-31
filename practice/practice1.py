class DatabaseConnection:
    def __init__(self, name: str):
        self.name = name
        self.is_open = False

    def open(self) -> None:
        self.is_open = True
        print(f"Connection to {self.name} opened")

    def close(self) -> None:
        self.is_open = False
        print(f"Connection to {self.name} closed")

    def query(self, sql: str) -> None:
        if "DROP" in sql:
            raise ValueError("Dangerous query blocked!")
        print(f"Running: {sql}")


def run_query(db: DatabaseConnection, sql: str):
    db.open()
    try:
        db.query(sql)
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        db.close()


run_query(DatabaseConnection("users_db"), "DROP TABLE users")
