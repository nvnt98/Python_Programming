# chapter11.py
def mean(xs: list[float]) -> float:
    """Return arithmetic mean. Pure: no side effects."""
    if not xs:
        raise ValueError("mean of empty list")
    return sum(xs) / len(xs)

def add_all(*args: int) -> int:
    return sum(args)

def configure(**options):
    return options

# Scope (LEGB) + globals/nonlocal
counter = 0

def tick():
    global counter
    counter += 1

def make_adder(delta: int):
    total = 0
    def add(x: int) -> int:
        nonlocal total
        total += delta
        return x + total
    return add

# Mutable default pitfall
def append_bad(x, bucket=[]):
    bucket.append(x)
    return bucket

def append_good(x, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(x)
    return bucket
