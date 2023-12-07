

class Customer:
    allCustomers = []
    
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        Customer.addToAllCustomers(self)
        
    def given_name(self):
        return f"{self.firstName}"
    
    def family(self):
        return f"{self.lastName}"
    
    def full_name(self):
        return f"{self.firstName} {self.lastName}"
    
    @classmethod
    def addToAllCustomers(cls, customer):
        cls.allCustomers.append(customer)
        
    @classmethod
    def all(cls):
        return cls.allCustomers
    
    
c1 = Customer("John", "Doe")
c2 = Customer("John", "Doe")
print(c1.given_name())
print([item.firstName for item in Customer.allCustomers])
print(Customer.all())
