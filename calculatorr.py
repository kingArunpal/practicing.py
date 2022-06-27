  


class calculator:
    a=int(input("enter a number to calculate"))
    b=int(input("enter another number to calculate"))

    def sum (self,a,b):
        c= a+b
        print(c)
    def sub (self,a,b):
        d=a-b
        print (d)
    def multiply (self,a,b):
        e=a*b
        print(e)
    def devision (self,a,b):
        f=a/b 
        print(f)
class calculatornew (calculator):
    def modulus (self,a,b):
        g= a%b 
        print(g)
    def exponential (self,a,b):
        h=a**b
        print (h)
    def floordivision(self,a,b):
        i=a//b
        print(i)

obj=calculatornew()

obj.sum(obj.a,obj.b)
obj.sub(obj.a,obj.b)
obj.multiply(obj.a,obj.b)
obj.devision(obj.a,obj.b)
obj.modulus(obj.a,obj.b)
obj.exponential(obj.a,obj.b)
obj.floordivision(obj.a,obj.b)