'''
Methods of List
'''

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
# Output: [1, 2, 3, 4]

my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)
# Output: [1, 2, 3, 4, 5]

my_list = [1, 2, 4]
my_list.insert(2, 3)
print(my_list)
# Output: [1, 2, 3, 4]

my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)
# Output: [1, 3, 2]

my_list = [1, 2, 3]
val = my_list.pop()
print(val, my_list)
# Output: 3 [1, 2]

my_list = [1, 2, 3]
my_list.clear()
print(my_list)
# Output: []

my_list = [10, 20, 30]
print(my_list.index(20))
# Output: 1

my_list = [1, 2, 2, 3, 2]
print(my_list.count(2))
# Output: 3

my_list = [3, 1, 2]
my_list.sort()
print(my_list)
# Output: [1, 2, 3]

my_list.sort(reverse=True)
print(my_list)
# Output: [3, 2, 1]

my_list = [1, 2, 3]
my_list.reverse()
print(my_list)
# Output: [3, 2, 1]

original = [1, 2, 3]
new_list = original.copy()
new_list.append(4)
print(original, new_list)
# Output: [1, 2, 3] [1, 2, 3, 4]


'''
Methods of Tuple
'''

my_tuple = (1, 2, 2, 3, 2)
print(my_tuple.count(2))
# Output: 3

my_tuple = (10, 20, 30)
print(my_tuple.index(30))
# Output: 2

my_tuple = (1, 2, 3)
my_tuple[0] = 99
# Output: TypeError: 'tuple' object does not support item assignment


'''
 Methods of Set 
'''

s = {1, 2, 3}
s.add(4)
print(s)
# Output: {1, 2, 3, 4}

s = {1, 2}
s.update([3, 4])
print(s)
# Output: {1, 2, 3, 4}

s = {1, 2, 3}
s.remove(2)
print(s)
# Output: {1, 3}

s.remove(99)
# Output: KeyError: 99

s = {1, 2, 3}
s.discard(99)
print(s)
# Output: {1, 2, 3}

s = {1, 2, 3}
val = s.pop()
print(val, s)
# Output (order may vary): 1 {2, 3}

s = {1, 2, 3}
s.clear()
print(s)
# Output: set()

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
# Output: {1, 2, 3, 4, 5}

a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))
# Output: {2, 3}

a = {1, 2, 3}
b = {2, 3, 4}
print(a.difference(b))
# Output: {1}

a = {1, 2, 3}
b = {2, 3, 4}
print(a.symmetric_difference(b))
# Output: {1, 4}

a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))     # Output: True
print(b.issuperset(a))   # Output: True
print(a.isdisjoint({9})) # Output: True


'''
Methods of Frozenset

'''

fs = frozenset([1, 2, 2, 3])
print(fs)
# Output: frozenset({1, 2, 3})

fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])
print(fs1.union(fs2))
# Output: frozenset({1, 2, 3, 4, 5})

print(fs1.intersection(fs2))
# Output: frozenset({3})

print(fs1.difference(fs2))
# Output: frozenset({1, 2})

print(fs1.symmetric_difference(fs2))
# Output: frozenset({1, 2, 4, 5})

fs3 = frozenset([1, 2])
print(fs3.issubset(fs1))     # Output: True
print(fs1.issuperset(fs3))   # Output: True
print(fs3.isdisjoint(fs2))   # Output: True

"""
Methods of Dictionary

"""

d = {"a": 1, "b": 2}
print(d.get("a"))       # Output: 1
print(d.get("z", 0))    # Output: 0

d = {"a": 1, "b": 2}
print(list(d.keys()))
# Output: ['a', 'b']

print(list(d.values()))
# Output: [1, 2]

print(list(d.items()))
# Output: [('a', 1), ('b', 2)]

d = {"a": 1}
d.update({"b": 2, "c": 3})
print(d)
# Output: {'a': 1, 'b': 2, 'c': 3}

d = {"a": 1, "b": 2}
val = d.pop("a")
print(val, d)
# Output: 1 {'b': 2}

d = {"a": 1, "b": 2}
print(d.popitem())
# Output: ('b', 2)

d = {"a": 1}
d.setdefault("b", 2)
print(d)
# Output: {'a': 1, 'b': 2}

d = {"a": 1, "b": 2}
d.clear()
print(d)
# Output: {}

d1 = {"a": 1}
d2 = d1.copy()
d2["b"] = 2
print(d1, d2)
# Output: {'a': 1} {'a': 1, 'b': 2}

keys = ["x", "y", "z"]
d = dict.fromkeys(keys, 0)
print(d)
# Output: {'x': 0, 'y': 0, 'z': 0}