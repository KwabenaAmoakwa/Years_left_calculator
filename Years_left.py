from datetime import date

Date_of_birth = input("input your date of birth in this format(dd-mm-yyyy):\n")
today = str(date.today())

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
    elif mm2==x2:
        total_days2 += i - dd2
    x2+=1

#calculating the number of years between date of birth and current day
total_years = yy2 - (yy + 1)



total_days_alive = total_days + total_days2 + (total_years * 365)
total_days_left = 36500 - total_days_alive

years = total_days_left//365
months = (total_days_left - (years * 365))//30
days = total_days_left-((years * 365) + (months * 30))

print(f"You currently have {years} years, {months} months and {days} days left")