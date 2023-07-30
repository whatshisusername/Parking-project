import pywhatkit
import datetime
now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)
pywhatkit.sendwhatmsg("+919372135687","hiii bro",now.hour,now.minute+1)

