import random
import sys
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.on = False
        self.key = "off"
        
    def put_key(self):
        self.key = "on"
    
    def flip_key(self):
        if self.on == False:
            if self.key == "on":
                if not random.randint(1,10) == 1:
                    return "failed"
                else:
                    self.on = True
                    return "success"
        else:
            self.on = False
            return "turned off"
        
car = Car("A", "red")
print("car created")

car.put_key()
print("put key in car now")
success = car.flip_key()
i = 0
while not success == "success":
    i+=1
    print("failed to turn car on")
    success = car.flip_key()
    if i > 10:
        print("screw this crap")
        sys.exit(100)

print("car is on now vroom vroom")