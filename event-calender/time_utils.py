REF_YEAR = 2024
REF_MONTH = 9
REF_DATE = 22
REF_HOUR = 00

# date format: DD/MM/YYYY
# time format: HH:MM
def getMinuteEquivalentOfDate(dateStr, timeStr):
    [dds, mms, yyyys] = dateStr.split("/")
    [dd, mm, yyyy] = [int(dds), int(mms), int(yyyys)]
    
    [hs, mss] = timeStr.split(":")
    [hh, ms] = [int(hs), int(mss)]

    return (yyyy-REF_YEAR)*365*24*60 + (mm-REF_MONTH)*30*24*60 + (dd-REF_DATE)*24*60*60 + (hh-REF_HOUR)*60 + ms

def getHourOfTheDay(minutes):
    return (minutes%(24*60))//60

def getMinuteOfTheHour(minutes):
    return minutes%60

def getMinutesForTheDay(minutes):
    return minutes%(24*60)