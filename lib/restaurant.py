

class Restaurant:
    def __init__(self, name):
        self._name = name
        
    def name(self):
        return self._name
    
r1 = Restaurant("Figo")
print(r1.name())