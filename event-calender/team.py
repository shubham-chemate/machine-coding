from slot import Slot

class Team:
    def __init__(self, id):
        self.id = id
        self.members = []
        self.bookedSlots = []

    def __str__(self):
        slotstr = ""
        for slot in self.bookedSlots:
            if len(slotstr) > 0:
                slotstr += "\n"
            slotstr += str(slot)
        memberstr = ""
        for member in self.members:
            if len(memberstr)>0:
                memberstr += "\n"
            memberstr += str(member)
        return f'ID:{self.id} \nMembers:\n{memberstr} \nSlots:\n{slotstr}'

    # GETTERS AND SETTERS

    def addMember(self, member):
        if not member.addToTeam(self.id):
            return False
        self.members.append(member)
        return True

    def removeMembers(self, memberId):
        pass

    # FUNCTIONALITIES

    def isFree(self, startTime, endTime):
        cnt = 0
        for member in self.members:
            if member.isFree(startTime, endTime):
               cnt += 1 
        return cnt
    
    def blockTime(self, startTime, endTime, eventId, cnt):
        for member in self.members:
            if not member.isFree(startTime, endTime):
                continue
            member.blockTime(startTime, endTime, eventId)
            cnt -= 1
            if cnt==0:
                break
        slot = Slot(startTime, endTime, eventId)
        self.bookedSlots.append(slot)

    def getAvailableSlots(self, startTime, endTime, reqCnt):
        lst = [0]*(endTime-startTime+1)
        for member in self.members:
            availableSlots = member.getAvailableSlots(startTime, endTime)
            for slot in availableSlots:
                for t in range(slot[0], slot[1]+1):
                    if t >= startTime and t<=endTime:
                        lst[t-startTime]+=1

        slots = []
        for t in range(len(lst)):
            if lst[t]<reqCnt:
                continue

            if len(slots)!=0 and t+startTime==slots[-1][1]+1:
                slots[-1][1]+=1
            else:
                slots.append([t+startTime, t+startTime])

        return slots
