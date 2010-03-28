import datetime

firstsundays = 0

d = datetime.date(1901,1,1)
while d <= datetime.date(2000,12,31):
    if d.day == 1 and d.weekday() == 6:
        firstsundays += 1
    d += datetime.timedelta(1)
print firstsundays