

class Test:

    def __init__(self,var1):
        self.var1 = var1
        self.var2 = 4
        var3 = 5

    def test(self):
        print("var1= %s" %self.var1)
        print("var2=" + str(self.var2))
        print("var3=" + str(self.var3))

    def test2(self):
        print(self.var2)


test = Test(1)
print(test.var1)
test.test()
