from cricketGame import CricketGame

def main():
    cricketGame = CricketGame(2, 5)
    cricketGame.addOrdering(1,[0, 1, 2, 3, 4])
    cricketGame.addOrdering(2,[0, 1, 2, 3, 4])

    ballsForTeam1 = [[1,1,1,1,1,2],["W",4,4,"Wd","W",1,6]]
    ballsForTeam2 = [[4, 6, "W", "W", 1, 1], [6, 1, "W", "W"]]

    print("****************")
    print("TEAM-1 BATTING")
    print("****************")
    for over in ballsForTeam1:
        print("OVER SCOREDCARD")
        for ball in over:
            cricketGame.playBall(1, ball)
        cricketGame.showBoard(1)
        print()

    cricketGame.showPlayers(1)

    print("\n\n\n\n")
    print("****************")
    print("TEAM-2 BATTING")
    print("****************")
    
    for over in ballsForTeam2:
        print("OVER SCOREDCARD")
        for ball in over:
            cricketGame.playBall(2, ball)
        cricketGame.showBoard(2)
        print()

    cricketGame.showPlayers(2)

    print("\n\n\n\n")
    cricketGame.printResult()


main()