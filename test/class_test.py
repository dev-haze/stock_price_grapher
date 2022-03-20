class C:
    v = 0
    def f(self,to):
        self.v = to


a = C()
b = C()

a.f(2)
b.f(3)

print(a.v)
print(b.v)

