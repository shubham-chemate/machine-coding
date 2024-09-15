class Player:
    def __init__(self, id):
        self.id = id
        self.runs = 0
        self.ballsFaced = []
        self.fours = 0
        self.sixes = 0

    def getId(self):
        return self.id
    
    def addBall(self, ball):
        self.ballsFaced.append(ball)
        if ball=="W":
            return

        self.runs += ball
        if (ball==4):
            self.fours+=1
        elif (ball==6):
            self.sixes+=1
    
    def showPlayer(self):
        print(f'[{self.id} => {self.runs}({len(self.ballsFaced)}), 4s:{self.fours}, 6s: {self.sixes}]')