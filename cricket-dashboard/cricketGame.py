from cricketTeam import CricketTeam

class CricketGame:
    def __init__(self, noOfOvers, playersPerTeam):
        self.noOfOvers = noOfOvers
        self.playersPerTeam = playersPerTeam
        
        self.team1 = CricketTeam(playersPerTeam)
        self.team2 = CricketTeam(playersPerTeam)

    def getTeam(self, id):
        if (id==1):
            return self.team1
        elif (id==2):
            return self.team2
        else:
            return None

    def addOrdering(self, team, ordering):
        self.getTeam(team).addOrdering(ordering)  

    def playBall(self, team, ball):
        self.getTeam(team).playBall(ball)

    def showPlayers(self, team):
        print(f'TEAM - {team} PLAYERS:')
        self.getTeam(team).showPlayers()

    def showBoard(self, team):
        self.getTeam(team).showBoard()

    def printResult(self):
        team1Score = self.team1.getTotalRunScored()
        team2Score = self.team2.getTotalRunScored()

        print("*************************")
        if (team1Score > team2Score):
            print("WINNER IS TEAM - 1")
            print(f"won by {team1Score-team2Score} runs")
        elif (team1Score < team2Score):
            print("WINNER IS TEAM - 2")
            print(f"won by {self.playersPerTeam-self.team2.getTotalWickets()} wickets")
        elif (team1Score == team2Score):
            print("DRAW")
        print("Congratulations to the winner team!")
        print("*************************")
