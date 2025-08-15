# chapter7.py
# range
for i in range(3):           # 0,1,2
    print(i)

for i in range(2, 10, 3):    # 2,5,8
    print(i)

# enumerate: index + value
letters = ["a", "b", "c"]
for idx, ch in enumerate(letters, start=1):
    print(idx, ch)

# zip: parallel iteration
xs = [1, 2, 3]
ys = [10, 20, 30]
for x, y in zip(xs, ys):
    print(x, y, x + y)

# Unzipping
pairs = list(zip(xs, ys))
ux, uy = zip(*pairs)   # tuples (1,2,3), (10,20,30)
