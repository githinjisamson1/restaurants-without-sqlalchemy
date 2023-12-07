
class Review:
    # keep track of instances
    allReviews = []
    allCustomers = []
    
    # Review constructor
    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self.rating = rating if type(rating) in (int, float) else "Rating must be a number"
        
     
        Review.addToAllReviews(self)
        Review.addToAllCustomers(customer)
        
    def rating(self):
        return self.rating
    
    @classmethod
    def addToAllReviews(cls, review):
        cls.allReviews.append(review)
        
    @classmethod
    def all(cls):
        return cls.allReviews
    
    def customer(self):
        return self._customer
    
    def restaurant(self):
        return self._restaurant
    
    @classmethod
    def addToAllCustomers(cls, customer):
        # avoid duplicates
        if customer not in cls.allCustomers:
            cls.allCustomers.append(customer)
        

# instatiation 
r1 = Review("John", "Figo", 4)
r3 = Review("John", "Figo", 4)
r4 = Review("Juliana", "Figo", 4)
# r2 = Review("Peter", "Abc", "k")

# test workig
# print([item.rating for item in Review.allReviews])
print(Review.all())
print(Review.allReviews)
print(r1.rating)
print(r1.customer())
r1.customer = "Jane"
print(r1.restaurant())