# variable = attributes

# instance of the class = means sache me se gujiya nikalna he bas 

class Car:
    def __init__(self, brand, model): # __init__ is permenent construction
        self.brand = brand
        self.modek = model
        
    def full_name(self,name): # self mane telephone
        print ( {f"name": name})
        
my_car = Car("Tata", "Safari") # attribute
print(my_car.brand)
print(my_car.modek)
    