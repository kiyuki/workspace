"""
import collections

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print("type s, list contains tuple?",s)
print("type in list", type(s[0]))

d = collections.defaultdict(list)
print("d", d)
print("type of d", type(d))
for k, v in s:
    print("k, v",k, v)
    d[k].append(v)
print(sorted(d.items()))


t = "mississippi"
u = collections.defaultdict(int)
for k in t:
    u[k] += 1
print(sorted(u.items()))

print("__________________________v")

w = {}
for k, v in s:
    w.setdefault(k, []).append(v)
print(w.items())
print(sorted(w.items()))
"""