# chapter6.py
nums = [10, 20, 30, 40, 50]
print(nums[0], nums[-1])           # 10, 50
print(nums[1:4])                   # [20, 30, 40]
print(nums[:3], nums[3:])          # [10,20,30], [40,50]
print(nums[::2])                   # [10, 30, 50] (step)
nums[1:3] = [21, 31, 999]          # splice replacement
print(nums)                        # [10, 21, 31, 999, 40, 50]

# Copy vs aliasing
a = [1, 2, 3]
b = a           # alias
c = a[:]        # shallow copy
a.append(4)
print(b)        # [1,2,3,4] changed (same object)
print(c)        # [1,2,3] not changed

# Comprehensions
squares = [x*x for x in range(6) if x % 2 == 0]
