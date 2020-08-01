class A:
    def f(self):
        print(self)
        print(hex(id(self)))

a = A()
a.f()
