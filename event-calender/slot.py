class Slot:
    def __init__(self, startTime, endTime, eventId):
        self.startTime = startTime
        self.endTime = endTime
        self.eventId = eventId

    def getStartTime(self):
        return self.startTime
    
    def getEndTime(self):
        return self.endTime
    
    def getEventId(self):
        return self.eventId
    
    def __str__(self):
        return f'({self.startTime}, {self.endTime}, {self.eventId})'