class audi :
    

    def Drive (self):
        
        print ("average 30km/liter")
    def brake (self):
        
        print("disk brake generation 1")

    def Gearbox(self):
       
        print("manual gare box with 4 gare")
    def Radio (self):
        
        print("generation 1 model radio")     

class audiadvance(audi) :

    def MusicSystem(self):
        
        print ("bluetooth,pendrive,auxicable,radio")

    def Gearbox1(self):

        print ("autometic gears 5")
    def rooftop(self):

        print ("automatic rooftop")

        
obj=  audiadvance()


obj.MusicSystem()
obj.Gearbox1()
obj.Drive()
obj.brake()
obj.rooftop() 