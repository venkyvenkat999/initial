"""from datetime import datetime
now=datetime.now()
timeDate=now.strftime("%d:%m:%y:%h:%m:%s")
print("time date is:",timeDate)
print("now=",now)
today=date.today()
d1=today.strftime("%d/%m/%y")
print("today:",d1)
"""
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	