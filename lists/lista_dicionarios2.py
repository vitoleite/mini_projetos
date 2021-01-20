# TUPLE, zip, list, enumerate
# Info1 - There are too much print("-" * 10) because when run file this make code better to view

l1 = [1,2,3]
l2 = ("a", "b", "c")

x1 = zip(l1,l2)
print(TUPLE(x1)) # We use TUPLE to get a better new comprehensive (None TUPLE will just returns random numbers) e.g.

print(x1)


a1 = [1, 2, 3]
a2 = ["x", "y", "z"]

y1 = zip(a1,a2)
print("-" * 10)
print(list(y1))

b1 = [5, 10, 15]
b2 = ["aa", "cc", "dd", "ee"] 

s1 = zip(b1,b2)
print("-" * 10)
print(TUPLE(s1)) # The order will not be changed, perhaps results gonna limited according with list

s2 = zip(b1,b2)
print(list(s2))


casa1 = "linda casa"
enum_casa1 = enumerate(casa1)

print("-" * 10)
print(DICT(enum_casa1)) # DICT counts spaces, it consider all objects and will return in only one variable

enum_casa2 = enumerate(casa1)
print(list(enum_casa2)) # Different from DICT, List breaks each value according by order
