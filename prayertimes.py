import sqlite3
from datetime import date



def get_day():
    now = date.today()
    jan = date(now.year,1,1)
    diff = now - jan
    return diff.days


def connect_db():
     conn = sqlite3.connect("salat.db")
     return conn


def convert_time(minutes):
    hours = minutes //60
    mins = minutes % 60
    hoursvalue = str(hours).rjust(2,"0")
    minsvalue =   str(mins).rjust(2,"0")
    timeString = str(hoursvalue) +":" + str(minsvalue)
    return timeString


#the function above return the prayer times for the given catogoryId
def get_prayerTimes(categoryId,days):   
    connection = connect_db()
    c = connection.cursor()
    c.execute("select Fajuru,Sunrise,Dhuhr,Asr,Maghrib,Isha from PrayerTimes where CategoryId=? and Date=?",[categoryId,days])
    Times = c.fetchone()
    prayers = ["Fajuru","Sunrise","Dhuhr","Asr","Maghrib","Isha",]
    prayerTimes = {}
    for i in range(0,6):
        ftime = convert_time(Times[i])
        #print(ftime)
        prayerTimes[prayers[i]] = ftime
    connection.close()

    return(prayerTimes)



#namaadhTimes = get_prayerTimes(45)




