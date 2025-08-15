# chapter5.py
def grade(score):
    if not (0 <= score <= 100):
        return "invalid"
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"

# Guard clauses for clarity
def safe_div(a, b):
    if b == 0:
        return None
    return a / b

# Structural pattern matching (Python 3.10+)
def describe_point(p):
    match p:
        case (0, 0):
            return "origin"
        case (x, 0):
            return f"x-axis at {x}"
        case (0, y):
            return f"y-axis at {y}"
        case (x, y):
            return f"point({x}, {y})"
