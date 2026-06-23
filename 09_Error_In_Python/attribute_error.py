# def function_name(parameter: type) -> return_type:
class car: 
    def __init__(self,brand: str) -> None:
        self.brand = brand
    
volvo: car = car(brand='volvo')
print(volvo.brand)
#Attribute error - when the attribute for the object doesn
#exist and there is nothing to use in dot.notation
# print(volvo.fuel_type) 


def func() -> None:
    ...

func().hello