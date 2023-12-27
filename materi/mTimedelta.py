# from datetime import datetime
from datetime import timedelta
import datetime

currentDate = datetime.now()
print(currentDate)

currentDate = datetime.now()
print(currentDate.day)

currentDate = datetime.now()
print(currentDate.month)

currentDate = datetime.now()
print(currentDate.year)

currentDate = datetime.now()
print(currentDate.strftime("%d"))

noww = datetime.now()

tipeDatatime = noww.year
print(tipeDatatime)
print("Ini tipe data ", type(tipeDatatime), "\n")

tipeStrin = noww.strftime("%Y")
print(tipeStrin)
print("Ini tipe data ", type(tipeStrin), "\n") 

str1 = '2022-12-31'
date1 = datetime.strptime(str1, "%Y-%m-%d")

print(date1.month)

currentDate = datetime.datetime.now()
dateAfter10days = currentDate + timedelta(days = 10)

print("Today date: ", currentDate.date())
print("Date after 10 days: ", dateAfter10days.date())