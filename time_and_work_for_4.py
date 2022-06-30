
x=float(input("enter number of days taken by A to complete the work "))
y=float(input("enter number of days taken by B to complete the work "))
z=float(input("enter number of days taken by C to complete the work "))
H=float(input("enter number of days taken by D to complete the work "))


def compute_lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm1 = greater
           break
       greater += 1

   return lcm1
compute_lcm(x, y)


def compute_lcmm(z, H):

   if z > H:
       greater = z
   else:
       greater = H

   while(True):
       if((greater % z == 0) and (greater % H == 0)):
           lcm2 = greater
           break
       greater += 1

   return lcm2
compute_lcmm(z,H)


def compute_lcmmm(lcm1,lcm2):

   if lcm1 > lcm2:
       greater = lcm1
   else:
       greater = lcm2

   while(True):
       if((greater % lcm1 == 0) and (greater % lcm2 == 0)):
           lcm_final = greater
           break
       greater += 1

   return lcm_final
   
print("total units of work to do by all together A, B, C, D is", compute_lcmmm(compute_lcm(x, y) ,compute_lcmm(z, H) ),"units")



def work(lcm_final):
      eff1=lcm_final/x
      eff2=lcm_final/y
      eff3=lcm_final/z
      eff4=lcm_final/H
      total_time =lcm_final/(eff1+eff2+eff3+eff4)
      print("total time taken by A,B,C,D is",total_time,"days")
work ( compute_lcmmm(compute_lcm(x, y),compute_lcmm(z, H) ) )