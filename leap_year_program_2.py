l=int(input("enter a year to check if that year is leap or not"))

if l % 4 == 0 and l % 100 !=0 :
    print ("the year",l ,"is a leap year")
elif l % 400 == 0:
    print ("the year",l ,"is a leap year")
elif  l % 100 == 0:
    print("the year",l ,"is not a leap year")

else:
    print("the year",l ,"is not a leap year")