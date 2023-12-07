

class Customer:
    all = []
    
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        Customer.addToAll(self)
        
    def given_name(self):
        return f"{self.firstName}"
    
    def family(self):
        return f"{self.lastName}"
    
    def full_name(self):
        return f"{self.firstName} {self.lastName}"
    
    @classmethod
    def addToAll(cls, customer):
        cls.all.append(customer)
    
    
c1 = Customer("John", "Doe")
print(c1.given_name())
print([item.firstName for item in Customer.all])
