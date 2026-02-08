class animal:
    def __init__(self,name,brand):
        self.name =name
        self.brand =brand
    
    def carname(self):
        print(f"the name of this car is {self.name}")

    def carbrand(self):
        print(f"the brand of this car is {self.brand}")    

car1 = animal("tesla","electro")  

car1.carbrand()
car1.carname()