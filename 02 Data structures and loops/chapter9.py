# chapter9.py
# While loop with sentinel
def read_until_blank():
    lines = []
    while True:
        s = input("line (blank to stop): ")
        if s == "":
            break
        lines.append(s)
    return lines

# Tuples & unpacking
pt = (3, 4)
x, y = pt
x, y = y, x   # swap

# Sets: uniqueness & fast membership
seen = set()
for ch in "abracadabra":
    seen.add(ch)
print(seen)  # order not guaranteed

# Operations
A = {1, 2, 3}
B = {3, 4}
print(A | B)  # union
print(A & B)  # intersection
print(A - B)  # difference
print(A ^ B)  # symmetric diff
