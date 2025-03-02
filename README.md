# Learning classes
* a repository for me to learn how to make classes in python.
* I'll try to explain everything i understood about classes in this readme file.
* why? because i want to. also, to learn git.

1 - car.py (02/03/2025)
```
class Car: # creates the car class
    def __init__(self, model, color): # constructs the instance
        self.model = model # this instance has the model {model}
        self.color = color
        self.on = False
        self.key = "off"
        
    def put_key(self): # self is for this instance
        self.key = "on"
    
    def flip_key(self): # self is for this instance
        if self.on == False: #if the car isnt on, 
            if self.key == "on": #see if the key is in the ignition,
                if not random.randint(1,10) == 1: # is the car going to fail? (probably)
                    return "failed"
                else:
                    self.on = True #the car didn't fail, so the car is on now
                    return "success"
        else:
            self.on = False # the car was on, so the car is off now
            return "turned off"
```
