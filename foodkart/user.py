from order import Order

class User:

    def __init__(self, name, gender, phNo, pin):
        self.id = phNo
        self.name = name
        self.gender = gender
        self.phNo = phNo
        self.pin = pin

    def addOrder(self, restId, foodId, quantity):
        self.orders.append(Order(restId, foodId, quantity))

    def getId(self):
        return self.id
    
    def getPin(self):
        return self.pin