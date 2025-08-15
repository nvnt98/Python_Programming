# chapter4.py
def read_int(prompt="Enter an integer: "):
    while True:
        s = input(prompt).strip()
        if s.lower() in {"q", "quit"}:
            raise KeyboardInterrupt("User quit")
        try:
            return int(s)
        except ValueError:
            print("Invalid integer. Try again or type 'q' to quit.")

age = read_int("Your age: ")
print(f"In five years, you’ll be {age + 5}.")
