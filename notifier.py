import datetime
import time
from datetime import date
import prayertimes
from win10toast import ToastNotifier


#this function must compare the time diffrence between two times and return diffrence

def compare_time(inputtime):
    current_date =  date.today()
    current_time = datetime.datetime.now()
    #currrent_time is now a time object

    prayer_time = datetime.datetime.strptime(inputtime,'%H:%M').time()
    prayer_datetime = datetime.datetime.combine(current_date, prayer_time)
    print(current_time)
    diff = prayer_datetime - current_time
    minutes = diff.seconds/60
    
    return minutes



def find_closest():
    timekeys = ["Fajuru","Sunrise","Dhuhr","Asr","Maghrib","Isha"] 
    day = prayertimes.get_day()
    r_times = prayertimes.get_prayerTimes(45,day)
    timearray = []
    for i in timekeys:
        timearray.append(r_times[i])

    print (timearray)
    today = date.today()
    c_time = datetime.datetime.now()
    print(c_time)
    closest = min([ i for i in timearray if datetime.datetime.combine(today,datetime.datetime.strptime(i, "%H:%M").time())  >= c_time], key=lambda t: abs(c_time - datetime.datetime.combine(today,datetime.datetime.strptime(t, "%H:%M").time()) ))
    prayerindex = timearray.index(closest)
    prayername = timekeys[prayerindex]
    diff = datetime.datetime.combine(today,datetime.datetime.strptime(closest, "%H:%M").time()) - c_time
    return diff.seconds,prayername
    




while 1==1:
    time.sleep(60)
    closest_prayer = find_closest()
    c = 10
    if closest_prayer[0] <= 120:
        toaster = ToastNotifier()
        toaster.show_toast("Prayer Alert",
                   "{0} prayer in 2 Minutes".format(closest_prayer[1]),
                   icon_path="mosque.ico",
                   duration=120)
    else:
        pass


