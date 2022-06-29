# Given a number, write a function to output its reverse digits. 
# (e.g. given 456 the answer is 654) Make sure that if it is a negative number  
# you keep the negative in the front (-456 becomes -654)

n=str(input("enter a number."))
def reverse_no(n):
    if str(n)[0] == '-':
        a = -1*int(''.join(reversed(str(n)[1:])))
    else:
        a = int(''.join(reversed(str(n))))
    print(a) 
reverse_no(n)