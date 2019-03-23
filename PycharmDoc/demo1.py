class Demo:
    var1 = 0
    var2 = 0
    var3 = 0

    def __init__(self, var1):
        self.var1 = var1
        print(self.var1)
        # self.var2 = 4
        var3 = 5

    def demo(self):
        self.var1 = 10
        var2 = 20
        self.var3 = 30

    def demo2(self):
        print(self.var2)

    def print(self):
        print("var1=" + str(self.var1))
        print("var2=" + str(self.var2))
        print("var3=" + str(self.var3))

    class Demo111:
        def asd(self):
            print("i'm demo111")
            Demo(111).print()


# demo = Demo(1)
# demo.demo()
# demo.print()
# demo2=Demo(1).Demo111()
# demo2.asd()
# demo2.print()
# demo2.print()

# d=list("hello")
# print(d)
# print(d.__getitem__(1))
# print(ord("b"))

a=False
b=2
print(a and b)
print(a or b)
