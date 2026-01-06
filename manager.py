import hashlib

class PasswordManager:
    def __init__(self):
        self.store = {}

    def _hash(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def save(self, service, password):
        self.store[service] = self._hash(password)

    def verify(self, service, password):
        return self.store.get(service) == self._hash(password)


def run():
    manager = PasswordManager()
    manager.save("email", "StrongPass123")
    manager.verify("email", "StrongPass123")


if __name__ == "__main__":
    run()
