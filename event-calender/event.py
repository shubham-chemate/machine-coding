from user import User
from team import Team

class Event:

    def __init__(self, id, startTime, endTime, representatives=0):
        self.id = id
        self.teamParticipants = []
        self.userParticipants = []
        self.startTime = startTime
        self.endTime = endTime
        self.reqRepresentatives = representatives

    # GETTERS AND SETTERS

    def getUser(self, id):
        pass

    def getTeam(self, id):
        pass

    def addUser(self, user:User):
        if not user.isFree(self.startTime, self.endTime):
            return False
        user.blockTime(self.startTime, self.endTime, self.id)
        return True

    def addTeam(self,team:Team):
        if team.isFree(self.startTime, self.endTime) < self.reqRepresentatives:
            return False
        team.blockTime(self.startTime, self.endTime, self.id, self.reqRepresentatives)
        return True