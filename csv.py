import serial
from statstics import mean
emotionalWellbeing=int(input("On a scale of 1-10 from sad to happy, how do you feel ? :"))
physicalWellbeing=int(input("On a scale of 1-10 from tired to full of energy, how do you feel ? :"))
socialWellbeing=int(input("On a scale of 1-10 from lonely to great, how would you rate your social wellbeing? :"))

averageScore = mean(emotionalWellbeing, physicalWellbeing, socialWellbeing)

print("Your average wellbeing score is", averageScore)

medianScore = median(emotionalWellbeing, physicalWellbeing, socialWellbeing)

print("The median of your score is", medianScore)

maxScore = max(emotionalWellbeing, physicalWellbeing, socialWellbeing)

print("The max of your score is", maxScore)

minScore = min(emotionalWellbeing, physicalWellbeing, socialWellbeing)

print("The max of your score is", minScore)

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM6'
ser.open()
while True:
    data = str(ser.readline())
    data=data.replace("b","")
    data=data.replace("'","")
    data=data.replace(" ","")
    data=data.replace("\\r\\n","")
    if len(data)>0:
        print(data)
        file = open("temperatures.csv",'a')
        file.write(data+"'")
        file.close()