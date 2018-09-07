def deco(func):
    def wrapper(*args, **kwargs):
        print('--start--')
        func(*args, **kwargs)
        print('--end--')
    return wrapper
@deco
def test():
    print('Hello Decorator')

test()

name ="lelouch"
print(id(name))
print(id(None) , "None")
print(id(True), "true")
print(id(False), "false")
name = None
print(id(name), "name None")
print (name == None)
myset1 = set([1,2,3])
myset2 = set([1,2,3,3,2,1])
print(myset1)
print(myset2)
firstset = set([1,1,1,1,1,1])
print(firstset)
firstset.add(4)
firstset.add(5)
print(firstset)
firstset.remove(1)
print(firstset)
firstset.clear()
print(firstset)

A={1,2,3}
B={3,4,5}
print(type(A), type(B))

C= A|B
print(C)

E= A&B
print(E, "E", "And set")
D = (1,2)
print(type(D), "D")
