from user import User
from team import Team
from event import Event
from time_utils import getMinuteEquivalentOfDate



def main():
    # user = User(1, 9, 17)
    # print(f'blocking time b/w 15-16: {user.blockTime(15, 16, 1)}')
    # print(f'blocking time b/w 14-15: {user.blockTime(13, 14, 1)}')

    # for slot in user.getBookingInfo():
    #     print(slot.getStartTime(), slot.getEndTime(), slot.getEventId())

    # print(getMinuteEquivalentOfDate("22/09/2024", "12:30"))

    dt = "22/09/2024"
    dtm = getMinuteEquivalentOfDate

    [A, B, C, D, E, F] = [
        User(1, dtm(dt, "10:00"), dtm(dt, "19:00")), #A
        User(2, dtm(dt, "09:30"), dtm(dt, "17:30")), #B
        User(3, dtm(dt, "11:30"), dtm(dt, "18:30")), #C
        User(4, dtm(dt, "10:00"), dtm(dt, "18:00")), #D
        User(5, dtm(dt, "11:00"), dtm(dt, "19:30")), #E
        User(6, dtm(dt, "11:00"), dtm(dt, "18:30"))] #F
    
    # C.blockTime(15, 16, 1)
    # C.blockTime(17, 18, 1)
    # C.blockTime(12, 13, 1)
    # E.blockTime(16*60+30, 17*60, 1)
    # print(C)
    # print(C.getAvailableSlots(11, 18))
    
    T1 = Team(1)
    T1.addMember(C)
    T1.addMember(E)

    T2 = Team(2)
    T2.addMember(B)
    T2.addMember(D)
    T2.addMember(F)

    dtn = "23/09/2024"


    print("\n######E1######")

    E1 = Event(1, dtm(dtn,"14:00"), dtm(dtn,"14:59"), 2)
    print(E1.addUser(A))
    print(E1.addTeam(T1))
    print(T1)

    # print("######E2######")

    # E2 = Event(2, dtm(dtn, "14:00"), dtm(dtn, "14:59"))
    # print(E2.addUser(C))

    print("\n######E3######")

    E3 = Event(3, dtm(dt, "15:00"), dtm(dt, "15:59"), 2)
    print(E3.addTeam(T1))
    print(E3.addTeam(T2))

    print(T1)
    print(T2)

    print("\n######E4######")

    E4 = Event(4, dtm(dt, "15:00"), dtm(dt, "15:59"), 1)
    print(E4.addUser(A))
    print(E4.addTeam(T2))

    print(A)
    print(T2)

    # print("######E5######")

    # E5 = Event(5, dtm(dt, "10:00"), dtm(dt, "10:59"))
    # print(E5.addUser(A))
    # print(E5.addUser(F))

    print("\n---EVENTS in current day 10 AM to next day 5 PM for User A")
    for slot in A.getEvents(dtm(dt, "10:00"), dtm(dtn, "17:00")):
        print(slot)

    print("\n---EVENTS in current day 10 AM to currnet day 5 PM for User B")
    for slot in B.getEvents(dtm(dt, "10:00"), dtm(dt, "17:00")):
        print(slot)

    print("\n---Available time slots for USER A")
    for slot in A.getAvailableSlots(dtm(dt, "00:00"), dtm(dt, "23:99")):
        print(slot)
    # A -> 10AM to 3PM and 4PM to 7PM

    print("\n---Available slots for team 1 with 1 reprentative")
    for slot in T1.getAvailableSlots(dtm(dt, "00:00"), dtm(dt, "23:99"), 1):
        print(slot)
    # C -> 11.30AM to 3PM and 4PM to 6.30PM
    # E -> 11.00AM to 3PM and 4PM to 7.30PM




if __name__=="__main__":
    main()