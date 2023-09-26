from datetime import date

# Date_of_birth = input("input your date of birth in this format(dd-mm-yyyy):")
# Your_age = int(input("input your age:"))
today = str(date.today())

Date_of_birth = "14-07-1992"

spl = Date_of_birth.split("-")
dd = int(spl[0])
mm = int(spl[1])-1
yy = int(spl[2])
total_days = 0
x= 0

spl2 = today.split("-")

yy2 = int(spl2[0])
mm2 = int(spl2[1])-1
dd2 = int(spl2[2])
total_days2 = 0
x2 = 0

days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]


#calculating number of days from date of birth till end of birth year
for i in days_in_months:
    if mm==x:
        total_days = i - dd
    elif mm<x:
        total_days += i
    x+=1
    
#calculating number of days from the beginning of the current year to the current day
for i in days_in_months:
    if mm2>x2:
        total_days2 += i
        print(total_days2)
    elif mm2==x2:
        total_days2 += i - dd2
    x2+=1
   
 
days_left = 36500 - total_days

years = days_left//365
months = (days_left - (years * 365))//12
days = days_left-((years * 365) + (months * 12))

#print(f"You currently have {days} days, {months} months, {years} years left")