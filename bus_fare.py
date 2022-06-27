# Write a program to calculate the fare of bus ticket ,
# 1) if the basefare of bus is rs.20, and On every 150 meters additional 0.75 rs will be added in it.

a=float(input("enter the distance in kms"))

def calculations(a):
    distance=a*( 1000)
    travelednoinmeters=distance/150
    additional_fair= 0.75*travelednoinmeters
    fair=4+additional_fair
    print (fair)

calculations(a)
