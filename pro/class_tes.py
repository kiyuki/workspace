class testClass():
    def __init__(self, message):
            self.value = message

class example():
    def __init__(self, a,b,c):
        self.num1 = a
        self.num2 = b
        self.num3 = c

    def print_tot(self):
        tot = self.num1 + self.num2 + self.num3
        print(tot)

class Oya():
    def __init__(self, a = "humean", b = 0):
        self.name = a
        self.age = b
    def oya_func(self):
        print("I am OYA")
        print(self.name, self.age)

class Kodomo(Oya):
    def kodomo_func(self):
        print("I am Kodomo")
        super().oya_func()

class Base:
    basevalue = "base"
    def spam(self):
        print("Base.spam()")

    def ham(self):
        print("ham")

class Derived(Base):
    def spam(self):
        print ("Derived.spam()")
        self.ham()

derived = Derived()
print("{0}".format(derived.basevalue))
derived.ham()
derived.spam()

k = Kodomo()
k.oya_func()
k.kodomo_func()
del k
myinstance2 = example(1,2,3)
myinstance2.print_tot()
myinstance = testClass("Hello!")
print(myinstance.value)
