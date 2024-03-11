import matplotlib as plt
print("*"*67)
print("*Please enter the time in seconds spent on your phone in session 1*")
print("*"*67)
pickUp1=int(input("*Please enter the time of pick-up 1:"))
print("*"*67)
pickUp2=int(input("*Please enter the time of pick-up 2:"))
print("*"*67)
pickUp3=int(input("*Please enter the time of pick-up 3:"))
print("*"*67)
pickUp4=int(input("*Please enter the time of pick-up 4:"))
print("*"*67)
pickUp5=int(input("*Please enter the time of pick-up 5:"))
print("*"*67)
pickUp6=int(input("*Please enter the time of pick-up 6:"))
print("*"*67)

print("*Please enter the time in seconds spent on your phone in session 2*")
print("*"*67)
pickUpOne=int(input("*Please enter the time of pick-up 1:"))
print("*"*67)
pickUpTwo=int(input("*Please enter the time of pick-up 2:"))
print("*"*67)
pickUpThree=int(input("*Please enter the time of pick-up 3:"))
print("*"*67)
pickUpFour=int(input("*Please enter the time of pick-up 4:"))
print("*"*67)
pickUpFive=int(input("*Please enter the time of pick-up 5:"))
print("*"*67)
pickUpSix=int(input("*Please enter the time of pick-up 6:"))
print("*"*67)

totalTime1=pickUp1+pickUp2+pickUp3+pickUp4+pickUp5+pickUp6
totalTime2=pickUpOne+pickUpTwo+pickUpThree+pickUpFour+pickUpFive+pickUpSix
fiveSessions=totalTime1*5
#This is to predict the total time that you would spend on your phone after five sessions with an alarm
fifthSession=totalTime2*5
#This is to predict the total time that you would spend on your phone after five sessions without an alarm
totalWasted=fifthSession+fiveSessions
#This shows the total amount of time wasted after five sessions
totalSaved=fifthSession-fiveSessions
#This takes away the predicted longer time from the shorter time to show time saved
averageSaved=(totalSaved)//5
#This shows the average time that you save per session
averageSpent=(fiveSessions)//5
#This shows the average time that you spend on your phone per session

if totalTime1<=300:
    print("*Your mood after session 1 was postive")

elif totalTime1>=301 and totalTime1<=1799:
    print("*"*67)
    print("*Your mood after session 1 was okay")
else:
    print("*"*67)
    print("*Your mood after session 1was poor")
    print("*"*67)
    
if totalTime2<=300:
    print("*"*67)
    print("*Your mood after session 2 was postive")
elif totalTime2>=301 and totalTime2<=1799:
    print("*"*67)
    print("*Your mood after session 2 was okay")
else:
    print("*"*67)
    print("*Your mood after session 2 was poor")
    print("*"*67)

if totalTime1<totalTime2:
    print("*"*67)
    print("*The removal of the incentive to use a mobile phone in the\n*workspace reduced the amount of time spent on a phone, made you\n*more productive and helped to positively affect your wellbeing by\n*improving your mood ;)")
    print("*"*67)
    print("*If you were to use this for your next 5 study or work sessions\n*you would spend",totalSaved,"seconds being more productive than if you\n*hadn't, and would spend\n*would gain an average of",averageSaved,"seconds per session.")
    print("*"*67)
    print("*You spent an average of",averageSpent,"seconds on your phone per session.\n*Although this is an improvement on your time spent on your\n*phone without the use of the message and an alarm we can\n*still work to improve this.\n*Improving this can help improve your mood which will\n*improve your mental wellbeing")
    print("*"*67)
elif totalTime1>=totalTime2:
    print("*"*67)
    print("*Unfortunatly the temptation of a mobile phone in a workspace is  *\n*too much for you to handle :( ,perhaps try removing the mobile  *\n*phone complelty from the workspace.\t\t\t\t  *")
    print("*"*67)
elif totalTime1>1799 and totalTime2>1799:
    print("*"*67)
    print("*Unfortunatly the temptation of a mobile phone in a workspace is  *\n*too much for you to handle :( ,perhaps try removing the mobile  *\n*phone complelty from the workspace.\t\t\t\t  *")
    print("*"*67)
    
alarm=[pickUp1, pickUp2, pickUp3, pickUp4, pickUp5, pickUp6]
noAlarm=[pickUpOne, pickUpTwo, pickUpThree, pickUpFour, pickUpFive, pickUpSix]
plt.plot(alarm)
plt.plot(noAlarm)
plt.legend(["Alarm", "No alarm"])
plt.title("No alarm")
plt.xlabel("Alarm")
plt.ylabel("Seconds")
plt.show()

session=7200
sessionSector=1200
#this is how much time spent working or studying per section. each section is 20 mins or 1200s
section1=sessionSector-pickUp1
section2=sessionSector-pickUp2
section3=sessionSector-pickUp3
section4=sessionSector-pickUp4
section5=sessionSector-pickUp5
section6=sessionSector-pickUp6

sectionOne=sessionSector-pickUpOne
sectionTwo=sessionSector-pickUpTwo
sectionThree=sessionSector-pickUpThree
sectionFour=sessionSector-pickUpFour
sectionFive=sessionSector-pickUpFive
sectionSix=sessionSector-pickUpSix

alarmed=[section1, section2, section3, section4, section5, section6]
notAlarmed=[sectionOne, sectionTwo, sectionThree, sectionFour, sectionFive, sectionSix]
plt.plot(alarmed)
plt.plot(notAlarmed)
plt.legend(["Alarm", "No alarm"])
plt.title("No alarm")
plt.xlabel("Alarm")
plt.ylabel("Seconds")
plt.show()