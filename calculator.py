
a= int  ( input ("enter a 1st number") ) 
b= int (input ("enter  a 2nd number") )
operation=input ("enter the operation")

class Tata :

    def Drive (self,a,b):
        c=a+b
        print (c)
    def Back (self,a,b):
        d=a-b
        print(d)

    def Gearbox(self,a,b):
        d=a/b
        print(d)
    def Radio (self,a,b):
        d=a/b
        print(d)     

class Safari2(Tata) :

    def eMusicSystem(self,a,b):
        c=a+b
        print (c)

obj=  Safari2()

obj.Radio(a,b)
obj.eMusicSystem()

        