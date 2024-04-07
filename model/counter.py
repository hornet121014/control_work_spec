class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            return False

        if self.count > 0:
            raise ValueError("Resource was not used in a resource block or was left open")

        return True