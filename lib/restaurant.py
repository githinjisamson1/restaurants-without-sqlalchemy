
from review import Review

class Restaurant:
    # Restaurant constructor
    def __init__(self, name):
        self._name = name
    
    # getter
    def name(self):
        return self._name
    
    # ORM
    def reviews(self):
        return [item for item in Review.allReviews]
    
    def customers(self):
        return [item for item in Review.allCustomers]
    
# instantiation
r1 = Restaurant("Figo")

# test
print(r1.name())
print(r1.reviews())
print(r1.customers())