from slot import Slot
import time_utils

class User:
    def __init__(self, id, startTime, endTime):
        self.id = id
        self.startTime = startTime
        self.endTime = endTime
        self.bookedSlots = []
        self.teamId = -1

    def __str__(self) -> str:
        slotstr = ""
        for slot in self.bookedSlots:
            if len(slotstr) > 0:
                slotstr += "\n"
            slotstr += str(slot)
        return f'{self.id}: {self.teamId} [{self.startTime}, {self.endTime}] \n{slotstr}'
    


    # GETTERS AND SETTERS

    def addToTeam(self, teamId):
        if self.teamId != -1:
            return False
        self.teamId = teamId
        return True
    
    def getId(self):
        return self.id
    
    def getStartTime(self):
        return self.getStartTime
    
    def getEndTime(self):
        return self.endTime
    
    def getBookingInfo(self):
        return self.bookedSlots
    

    
    # CORE FUNCTIONALITIES
    
    def isFree(self, timeFrom, timeTo):
        # timeFrom and timeTo should belong to working hours in any day
        if not self.isOverlap(timeFrom, timeTo, self.startTime, self.endTime):
            return False

        for slot in self.bookedSlots:
            if self.doTheyIntersect(timeFrom, timeTo, slot.getStartTime(), slot.getEndTime()):
                return False
        return True

    def blockTime(self, timeFrom, timeTo, eventId):
        # timeFrom and timeTo should belong to working hours in any day
        if not self.isOverlap(timeFrom, timeTo, self.startTime, self.endTime):
            return False

        if not self.isFree(timeFrom, timeTo):
            return False
        slot = Slot(timeFrom, timeTo, eventId)
        self.bookedSlots.append(slot)
        return True

    
    def getEvents(self, startTime, endTime):
        events = []
        for slot in self.bookedSlots:
            if self.doTheyIntersect(startTime, endTime, slot.getStartTime(), slot.getEndTime()):
                events.append(slot)
        return events
    
    def getAvailableSlots(self, startTime, endTime):
        if startTime < self.startTime:
            startTime = self.startTime
        if endTime > self.endTime:
            endTime = self.endTime

        # sort given slots
        # find gaps
        self.bookedSlots.sort(key=lambda x : x.getStartTime())

        lastFilled = startTime-1
        availableSlots = []
        for slot in self.bookedSlots:
            if slot.getStartTime()>endTime:
                if endTime-lastFilled>1:
                    availableSlots.append([lastFilled+1, endTime])
                    break
            diff = slot.getStartTime()-lastFilled
            if diff > 1:
                availableSlots.append([lastFilled+1, slot.getStartTime()-1])
            lastFilled = slot.getEndTime()
        return availableSlots
    





    # UTILITIES SUPPORT

    def doTheyIntersect(self, x1, y1, x2, y2):
        if x1<=x2 and x2<=y1:
            return True
        if x2<=x1 and x1<=y2:
            return True
        return False
    
    def isOverlap(self, x1, y1, x2, y2):
        l1 = time_utils.getMinutesForTheDay(x2)
        r1 = time_utils.getMinutesForTheDay(y2)

        l2 = time_utils.getMinutesForTheDay(x1)
        r2 = time_utils.getMinutesForTheDay(y1)

        return (l1<=l2 and r2<=r1)