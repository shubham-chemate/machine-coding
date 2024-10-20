from foodkart import FoodKart

def main():
    foodkart = FoodKart()

    foodkart.registerUser("Pranv", "M", "1", "HSR")
    foodkart.registerUser("Nitesh", "M", "2", "BTM")
    foodkart.registerUser("Vatsal", "M", "3", "BTM")

    foodkart.loginUser("1")

    foodkart.registerRest("FC1")
    foodkart.addPinToRest("FC1", ["HSR", "BTM"])
    foodkart.addFoodToRest("FC1", "NI Thali", 5, 100)

    foodkart.registerRest("FC2")
    foodkart.addPinToRest("FC2", ["BTM"])
    foodkart.addFoodToRest("FC2", "Burger", 3, 120)

    foodkart.loginUser("2")

    foodkart.registerRest("FC3")
    foodkart.addPinToRest("FC3", ["HSR"])
    foodkart.addFoodToRest("FC3", "SI Thali", 1, 150)

    foodkart.loginUser("3")
    foodkart.showRestaurants("price")

    print(foodkart.placeOrder("FC1", "NI Thali", 1))
    print(foodkart.placeOrder("FC2", "Burger", 7))

    foodkart.rateRest("FC2", 3, "Good Food")
    foodkart.rateRest("FC1", 5, "Nice Food")

    foodkart.showRestaurants("rating")

    foodkart.loginUser("1")
    foodkart.addFoodToRest("FC2", "Burger", 5, -1)
    # print(foodkart.placeOrder("FC2", "Burger", 7))

    foodkart.addPinToRest("FC2", ["BTM", "HSR"])

    foodkart.showRestaurants("price")


if __name__=="__main__":
    main()