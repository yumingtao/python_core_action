import time
import datetime


current_time = datetime.datetime.now()
print(int(datetime.datetime.timestamp(current_time)*1000))
print(int(time.mktime(current_time.timetuple())*1000))
