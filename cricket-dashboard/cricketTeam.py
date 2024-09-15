from player import Player
from functools import cmp_to_key

class CricketTeam:
    def __init__(self, playersCnt):

        self.yetToBatPlayers=[]
        self.outPlayers=[]
        self.battingPlayer=None
        self.oppPlayer=None

        self.ballsOrder = []
        self.ballsFaced = 0
        self.totalRunsScored = 0
        self.totalWickets = 0
        self.noBalls = []
        self.wides = []

        self.players = []
        for playerNo in range(playersCnt):
            player = Player(playerNo)
            self.players.append(player)

            self.yetToBatPlayers.append(player)

        self.battingPlayer = self.yetToBatPlayers[0]
        self.oppPlayer = self.yetToBatPlayers[1]
        self.yetToBatPlayers = self.yetToBatPlayers[2:]

    def getTotalRunScored(self):
        return self.totalRunsScored
    
    def getTotalWickets(self):
        return self.totalWickets

    def getPlayerById(self, id):
        for p in self.players:
            if p.getId()==id:
                return p
        return None

    # explicitly add ordering
    # or in the order as they added
    def addOrdering(self, order):
        ind = [-1 for _ in range(len(order))]
        for p in range(len(order)):
            ind[order[p]]=p
        self.players = sorted(self.players, key=cmp_to_key(lambda i1, i2 : ind[i1.getId()] - ind[i2.getId()]))
        self.yetToBatPlayers = self.players

        self.battingPlayer = self.yetToBatPlayers[0]
        self.oppPlayer = self.yetToBatPlayers[1]
        self.yetToBatPlayers = self.yetToBatPlayers[2:]

    def isAllOut(self):
        return self.totalWickets+1==len(self.players)

    def wicket(self):
        self.totalWickets+=1
        self.outPlayers.append(self.battingPlayer)
        if self.isAllOut():
            return

        self.battingPlayer = self.yetToBatPlayers[0]
        self.yetToBatPlayers = self.yetToBatPlayers[1:]

    def swapCreasePlayers(self, ball):
        if (ball=="W" or ball=="Wd" or ball=="Nb"):
            return

        if (ball%2==1):
            self.battingPlayer, self.oppPlayer = self.oppPlayer, self.battingPlayer

        if (self.ballsFaced%6==0):
            self.battingPlayer, self.oppPlayer = self.oppPlayer, self.battingPlayer

    def playBall(self, ball):
        self.ballsOrder.append(ball)
        if (ball=="W"):
            self.ballsFaced += 1
            self.battingPlayer.addBall(ball)
            self.wicket()
        elif (ball=="NB"):
            self.totalRunsScored += 1
            self.noBalls.append(ball)
        elif (ball=="Wd"):
            self.totalRunsScored += 1
            self.wides.append(ball)
        else:
            self.totalRunsScored += ball
            self.ballsFaced += 1
            self.battingPlayer.addBall(ball)

        if self.isAllOut():
            return
        
        print(f'ball: {ball}, batter: {self.battingPlayer.getId()}, opp: {self.oppPlayer.getId()}')
        self.showPlayer(self.battingPlayer.getId())
        self.showPlayer(self.oppPlayer.getId())
        
        self.swapCreasePlayers(ball)

    def showPlayers(self):
        for player in self.players:
            player.showPlayer()

    def showPlayer(self, id):
        for player in self.players:
            if (id==player.getId()):
                player.showPlayer()

    def showBoard(self):
        print("**************************")
        print(f'TOTAL RUNS: {self.totalRunsScored}')
        print(f'TOTAL WICKETS: {self.totalWickets}')
        print(f'TOTAL BALLS BOWLED: {self.ballsFaced//6}.{self.ballsFaced%6}')
        print(f'EXTRAS: no balls - {self.noBalls}, wides - {self.wides}')
        print("**************************")