import random
n= random.randint(1,100)
a= -1
gusses= 1

while a!=n:
 a=int(input("enter the number:"))
 if(a>n):
     print("too low")
     gusses +=1
 elif(a<n):
     print("too high")
     gusses +=1
 
 
 print(f"you have gussed the no {n} correctly in {gusses} attempts")    
     
