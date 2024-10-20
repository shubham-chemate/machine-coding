class Rating:
    def __init__(self, givenByUserId, stars, comment):
        self.givenByUserId = givenByUserId
        self.stars = stars
        self.comment = comment

    def getUserId(self):
        return self.givenByUserId
    
    def setStars(self, stars):
        self.stars = stars

    def setComment(self, comment):
        self.comment = comment