from user import User
from restaurant import Restaurant

class FoodKart:

    def __init__(self):
        self.users = []
        self.restaurants = []
        self.loggedInUserId = -1

    def placeOrder(self, restId, dishId, quantity):
        restaurant = self.getRestaurant(restId)
        if restaurant == None:
            return False
        
        return restaurant.orderDish(dishId, quantity)

    def registerUser(self, name, gender, phNo, pin):
        user = User(name, gender, phNo, pin)
        self.users.append(user)
        return True
    
    def loginUser(self, userId):
        self.loggedInUserId = userId

    def getUserDetails(self, id):
        for user in self.users:
            if user.getId()==id:
                return user
        return None
    
    def getRestaurant(self, id):
        for rest in self.restaurants:
            if id == rest.getId():
                return rest
            
        return None

    def registerRest(self, restId):
        if self.loggedInUserId == -1:
            return False

        userDetails = self.getUserDetails(self.loggedInUserId)
        restaurant = Restaurant(restId, userDetails.getId(), userDetails.getPin())

        self.restaurants.append(restaurant)

    def addFoodToRest(self, restId, foodId, quantity, price):
        restaurant = self.getRestaurant(restId)
        if restaurant == None:
            return False
        
        if restaurant.getOwnerId()!=self.loggedInUserId:
            return False
        
        return restaurant.addDish(foodId, quantity, price)
    
    def addPinToRest(self, restId, pins=[]):
        restaurant = self.getRestaurant(restId)
        if restaurant == None:
            return False
        
        for pin in pins:
            restaurant.addPin(pin)
    
    def rateRest(self, restId, stars, comment=""):
        restaurant = self.getRestaurant(restId)
        if restaurant == None:
            return False
        
        restaurant.rateRestaurant(self.loggedInUserId, stars, comment)

    def getRestaurants(self, pin):
        restaurants = []
        for restaurant in self.restaurants:
            if restaurant.isServable(pin):
                restaurants.append(restaurant)
        return restaurants

    def showRestaurants(self, filter):
        if self.loggedInUserId == -1:
            return False

        userDetails = self.getUserDetails(self.loggedInUserId)

        restaurants = self.getRestaurants(userDetails.getPin())

        if filter=="rating":
            # sort restaurant according to rating
            restaurants.sort(key=lambda x:x.getRating(), reverse=True)
            for restaurant in restaurants:
                for dish in restaurant.getDishes():
                    print(f'{restaurant.getId()} : {restaurant.getRating()} : {dish.getId()}')
        else:
            dishes = []
            for restaurant in restaurants:
                for dish in restaurant.getDishes():
                    dishes.append(tuple([dish.getPrice(),  dish.getQuantity(), dish.getId(), restaurant.getId()]))

            # sort dishes according to price
            dishes.sort(key=lambda x:x[0], reverse=True)

            for dish in dishes:
                print(dish)

