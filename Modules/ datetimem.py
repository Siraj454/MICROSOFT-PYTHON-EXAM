#In this Section we will work with Datetime module
#import module to time up your code
import datetime 
today=datetime.date.today()
year=today.year
day=today.day
month=today.month
#with time
now=datetime.datetime.now()
#print(today)
#print(year)
#print(day)
#print(month)
##to show result of above uncomment print statement by removing '#' sign
print(now.time())
print(now.month)
#standard format is year-month-day

print("*****Section_End*******")

#standard format is year-month-day(YYYY-MM-DD)
#conversion to desired formats
#to DD/MM/YYYY
print(now.strftime(" Today is %a %d %m %Y"))
#converting string to a date
birthday="02/11/2020"
new_bd=datetime.datetime.strptime(birthday,"%d/%m/%Y").date()
print("My birthday month is ",new_bd)
days_to_bd=new_bd-today
print(days_to_bd)
print(now.tzinfo)

#timedelta

print(now.time())
print(datetime.datetime.strftime(now,"%H:%m:%S"))
enrolled="07/02/87"
retired="06/02/19"
retired_n=datetime.datetime.strptime(retired,"%d/%m/%y").date()
enrolled_n=datetime.datetime.strptime(enrolled,"%d/%m/%y").date()
print("num of year month days ")
total_period=retired_n-enrolled_n
print(total_period/365)