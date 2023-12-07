
class Review:
    allReviews = []
    
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating if type(rating) in (int, float) else "Rating must be a number"
        
            
        Review.addToAllReviews(self)
        
    def rating(self):
        return self.rating
    
    @classmethod
    def addToAllReviews(cls, review):
        cls.allReviews.append(review)
        
    @classmethod
    def all(cls):
        return cls.allReviews
            
            
r1 = Review("John", "Figo", 4)
# r2 = Review("Peter", "Abc", "k")
print([item.rating for item in Review.allReviews])
print(Review.all())
print(Review.allReviews)
print(r1.rating)