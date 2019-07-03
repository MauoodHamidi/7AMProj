class test:
    def m1(self):
        self.a=1000
        self.b=2000
        def m2(self):
            print(self.a)
            print(self.b)
            x1=test()
            x1.m1()
            x1.m2()
            print(x1.a)
            print(x1.b)
            x2=test()
            x2.m1()
            x2.m2()