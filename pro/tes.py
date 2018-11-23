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
"""
l = ['Alice', 'Bob', 'Charlie']

for name in l:
    print(name)

print("______________")
for i, name in enumerate(l):
    print(i, name)
"""
"""
nodes = [0] * 10
con2 = range(10)
print("con", list(con2))
for a, con in enumerate(range(10)):
    nodes[a] = [0 if a < 5 else b*10 for b in con2 if b > 2 ]
print(nodes)

def tes(nodes, con,  k):
    pass
print("____________")
print( [i  for i in range(100) if i > 50])


from collections import namedtuple

Union = namedtuple('Union', 'l r') # 和
Produ = namedtuple('Produ', 'l r') # 積
Combi = namedtuple('Combi', 'e') # 組

a = Produ(l=Combi(e=1), r= 2)
print(a[0], a[1])
print(type(a[0]), type(a[1]))
print("Produ, type(a)", a, type(a))
"""
temp = map(int, input().strip().split())
print("Type of temp, temp",type(temp), list(temp))

