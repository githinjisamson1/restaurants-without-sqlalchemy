
from review import Review

class Customer:
    # keep track of instances
    allCustomers = []
    
    # Customer constructor
    def __init__(self, firstName, lastName):
        self._firstName = firstName
        self._lastName = lastName
        Customer.addToAllCustomers(self)
        
    # getters
    def given_name(self):
        return f"{self._firstName}"
    
    def family_name(self):
        return f"{self._lastName}"
    
    def full_name(self):
        return f"{self._firstName} {self._lastName}"
    
    # setters
    def setFirstName(self, firstName):
        self._firstName = firstName
        
    def setLastName(self, lastName):
        self._lastName = lastName
    
    # class methods
    @classmethod
    def addToAllCustomers(cls, customer):
        cls.allCustomers.append(customer)
        
    @classmethod
    def all(cls):
        return cls.allCustomers
    
    def restaurants(self):
        return [item for item in Review.allRestaurants]
    
    def add_review(self, restaurant, rating):
        # newReview is automatically added to allReviews
        newReview = Review(self.full_name(), restaurant, rating)
    
    # properties
    firstName = property(given_name, setFirstName)
    lastName = property(family_name, setLastName)
    
# instantiation/creating object
c1 = Customer("John", "Doe")
c2 = Customer("John", "Doe")

# changing lastName
c1.lastName = "Wentworth"

# test working
print(c1.given_name())
print(c1.full_name())
print([item.firstName for item in Customer.allCustomers])
print(Customer.all())
c1.add_review("zxcbnm", 3.9)
print(c1.restaurants())
