class DoorLock:
    def __init__(self, correct_code="1234"):
        self.state = "LOCKED"
        self.correct_code = correct_code
        self.attempts = 0

    def enter_code(self, code):
        if self.state == "LOCKED":
            if code == self.correct_code:
                self.state = "UNLOCKED"
                self.attempts = 0
                return "Door unlocked ✅"
            else:
                self.attempts += 1
                if self.attempts >= 3:
                    self.state = "BLOCKED"
                    return "Too many wrong attempts. System blocked ❌"
                return "Wrong code. Try again."

        elif self.state == "UNLOCKED":
            return "Door is already unlocked."

        elif self.state == "BLOCKED":
            return "System blocked. No more attempts allowed ❌"

    def lock(self):
        if self.state == "UNLOCKED":
            self.state = "LOCKED"
            return "Door locked 🔒"
        elif self.state == "LOCKED":
            return "Door already locked."
        elif self.state == "BLOCKED":
            return "System blocked. Cannot lock."


lock = DoorLock()

print(lock.enter_code("1111"))  # Wrong attempt 1
print(lock.enter_code("0000"))  # Wrong attempt 2
print(lock.enter_code("9999"))  # Wrong attempt 3 → BLOCKED
print(lock.enter_code("1234"))  # No longer accepted
