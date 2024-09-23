import turtle
from turtle import *
""" x = 3
y = float(3)
print(x,y)
values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)
print(values[6])
x = "this is a thing"
y= x.split( )
z = y[1]
print(y)
print(z)
x = "test"
print(f"hello {x}") """
""" temp = int(input(''))

if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" print("give me a number")
v = int(input(""))

if v % 2 == 0:
    print("even")
    
else:
    print("odd") """
""" print("how much is the bill?")   
b = int(input(''))
print("how is the service? (type bad,okay,good or,great)")
q = input("")

if q == "bad":
    print ("your bill is", b + b*0)

elif q == "okay":
    print ("your bill is", b + b*.15,("including a 15% tip"))

elif q == "good":
    print ("your bill is", b + b*.20,("including a 20% tip"))

elif q == "great":
    print ("your bill is", b + b*.25,("including a 25% tip")) """
""" Factors = []
print("give me a number")

number = int ( input (""))
for i in range(number):
    if number % (i + 1) == 0:
        Factors.append(i + 1)

print (Factors)
 """
number = int(input("give me a number "))
number2 = int(input("give me another number "))
CF = []
if number > number2:
    x = number
else:
    x = number2
for i in range(x):
    if number % (i + 1) == 0 and number2 % (i + 1) == 0:
        CF.append(i + 1)
print(max(CF))
