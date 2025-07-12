# exercise.py
# Part 1: Mutable vs Immutable
a = 100
b = a
print("Before:", a, b, id(a), id(b))

a += 1
print("After a += 1:", a, b, id(a), id(b))

x = [1, 2, 3]
y = x
print("Before:", x, y, id(x), id(y))

x.append(4)
print("After x.append(4):", x, y, id(x), id(y))
"""in the before both will have the same ID because b is = to a and both are looking at the same point. however the "after" A will be different from b because a is being changed while b is not. so b will maintain the same ID code while a doesn't.

for the lists both will be the same before and after. one because lists are mutable, and two because the list itself has an ID and all the "elements" in the list are under the same ID so adding or removing stuff to the list wont change the ID just the list itself."""
# ===

# Part 2: Lists & Loops
names = ["alice", "bob", "charlie", "dana"]

# Task A: build upper_names
upper_names = []
for n in names:
    upper_names.append(n.upper())
    pass

# Task B: enumerate over upper_names
for index, name in enumerate(upper_names_):
    print(index,name)
#    pass

# Task C: demo two list methods
# 1. insert
 upper_names.insert(1, "EVAN")
upper_names.insert(2, "HINATA")
# 2. remove
upper_names.remove("EVAN")
# 3. sort
upper_names.sort()
