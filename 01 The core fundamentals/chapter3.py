# chapter3.py
a, b = 7, 3
print(a / b)    # float division: 2.333...
print(a // b)   # floor division: 2
print(a % b)    # modulo: 1
print(a ** b)   # exponent: 343

# Comparisons chain naturally
x = 5
print(0 < x < 10)  # True

# Boolean: short-circuiting
user = "" or "guest"  # 'guest' because "" is Falsey
is_ok = True and (10 / 2 > 3)

# f-strings: readable formatting
name = "Navneet"
score = 9.5
print(f"Hello {name}, score={score:.2f}")     # 9.50
debug = 42
print(f"{debug=}")  # shows 'debug=42' (great for debugging)
