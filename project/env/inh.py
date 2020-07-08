class Abc():
    
    def __init__(self,param1=1):
        self.param1 = param1

    def prints1(self):
      return self.param1

class Cde(Abc):
    def __init__(self, param1=1):
        super().__init__(param1=param1)

if __name__ == "__main__":

    myabc = Abc(10)
    print(myabc.param1)
    mycde= Cde(10)
    print(myabc.prints1())
    print(mycde.prints1())
