
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
    
    def average_star_rating(self):
        # initialize to 0
        totalRating = 0
        
        # iterate Review.allReviews
        for item in Review.allReviews:
            totalRating += item.rating
            
        return totalRating/len(Review.allReviews)
    
# instantiation
r1 = Restaurant("Figo")

# test
print(r1.name())
print(r1.reviews())
print(r1.customers())
print(r1.average_star_rating())