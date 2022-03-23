# Python 3
# coding: utf-8
import os

__author__ = "Ammar S Malik"
__copyright__ = "Copyright 2022, Time calculations"
__credits__ = ["Ammar Malik"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "all creditors/github"
__email__ = "dev.malik.ammar@gmail.com"
__status__ = "Production"


os.system('clear')
# Input time
time = input("Enter time HH:MM:SS AM : ")
timeToAdd = input("Time to add in HH:MM:SS : ")

# Divide Hours, Minutes and Seconds for time and timeToAdd
extractAmPm = time.split(' ')
if len(extractAmPm) > 1 :
    originalTime = extractAmPm[0].split(':')
else:
    originalTime = time.split(':')

originalTimeToAdd = timeToAdd.split(':')

# Now add hours, minute and seconds to the original time to get 
# new time 
finalHour = int(originalTime[0])
finalMin = int(originalTime[1])
finalSec = int(originalTime[2])

# Before moving any further, see if we have AM/PM added to time or not. If there is
# Am/PM than we need to make it 24 hour clock and will determine Am/PM after the 
# calculations. If 12 AM than it shoud be 00. If 12 PM to 11PM than add 12 to it
cAmPm = ""
if len(extractAmPm) > 1 :
    cAmPm = extractAmPm[0].upper()
    if extractAmPm[0].upper() == "AM" and finalHour == 12:
        finalHour = 0
    elif extractAmPm[0].upper() == "PM" and finalHour >= 1 and finalHour <= 11:
        finalHour+=12
    else:
        finalHour=finalHour

# now add time to these valuse starting from seconds all the way to hours
finalSec+=int(originalTimeToAdd[2])

# now check if we went more that 59 seconds. If we did than how many times
# 120 seconds means we went over twice. 120/60 and the remainder is 0
# so it means it is 2 minutes. 
addTo = 0
if finalSec > 60 :  
    addTo = finalSec // 60      # What is the whole number or how many 60s we have here
    finalSec = finalSec % 60    # what is the remained after dividing it by 60

# Now calculate Minutes same way we calculated Seconds and see if we need to 
# move an hour or not
finalMin+=int(originalTimeToAdd[1]) + addTo
addTo = 0
if finalMin > 60 :  
    addTo = finalMin // 60      # What is the whole number or how many 60s we have here
    finalMin = finalMin % 60    # what is the remained after dividing it by 60

# now see how to manage hours 
finalHour+=(int(originalTimeToAdd[0])+addTo)

# now see if we need AM or PM at the end of the time
# if Time is more than 12 than it is PM, if it is more than 24 than it is am and also
# if it is less than 12 than it is AM

if finalHour <= 12:
    cAmPm = "AM"
elif finalHour < 23:
    cAmPm = "PM"
    finalHour-=12
else:
    cAmPm = "AM"
    while finalHour > 23 :
        finalHour-=24

print(f"Your time will be : {finalHour:02}:{finalMin:02}:{finalSec:02} {cAmPm}")