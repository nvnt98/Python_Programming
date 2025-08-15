# chapter2.py
age = 20                # int
pi = 3.14159            # float
title = "CSE Student"   # str
flag = True             # bool
nothing = None          # absence of value

# Equality vs identity
a = [1, 2]
b = [1, 2]
c = a
print(a == b)  # True (equal contents)
print(a is b)  # False (different objects)
print(a is c)  # True (same object)

# Truthiness rules
items = []
if items:      # empty list is Falsey
    print("has items")
else:
    print("empty")

# Common Falsey: 0, 0.0, "", [], {}, set(), range(0), None, False
