from rating import Rating
from food import Food

class Restaurant:

    def __init__(self, id, ownerId, ownerPin):
        self.id = id
        self.ownerId = ownerId
        # list of pincodes
        self.serveArea = []
        self.ratings = []
        self.dishes = []

    def getPins(self):
        return self.serveArea

    def getDishes(self):
        return self.dishes

    def getId(self):
        return self.id

    def getOwnerId(self):
        return self.ownerId

    def addPin(self, pin):
        if not pin in self.serveArea:
            self.serveArea.append(pin)

    def getRating(self):
        sum = 0
        cnt = 0
        for rating in self.ratings:
            sum += rating.stars
            cnt += 1
        return sum/cnt
    
    def isServable(self, pin):
        dishAval = False
        for dish in self.dishes:
            if dish.getQuantity()>0:
                dishAval = True
        return (pin in self.serveArea) and dishAval
    
    def orderDish(self, id, quantity):
        for dish in self.dishes:
            if dish.getId() == id and dish.getQuantity() > quantity:
                dish.reduceQuantity(quantity)
                return True
        return False
    
    def rateRestaurant(self, userId, stars, comment=""):
        for rating in self.ratings:
            if rating.getUserId()==userId:
                rating.setStars(stars)
                rating.setComment(comment)
                return

        self.ratings.append(Rating(userId, stars, comment))

    def addDish(self, id, quantity, price):
        for dish in self.dishes:
            if dish.getId()==id:
                dish.addQuantity(quantity)
                if price != -1:
                    dish.addPrice(price)
                return True
            
        self.dishes.append(Food(id, quantity, price))
        return True