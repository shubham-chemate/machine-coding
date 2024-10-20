class Food:
    def __init__(self, id, quantity, price):
        self.id = id
        self.quantity = quantity
        self.price = price

    def reduceQuantity(self, d):
        self.quantity -= d

    def getQuantity(self):
        return self.quantity
    
    def getId(self):
        return self.id
    
    def addQuantity(self, d):
        self.quantity += d

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price