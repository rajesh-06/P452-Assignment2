import mm1
import math as m
import matplotlib.pyplot as plt

#generating random numbers using multiplicative linear congruential generator method
a1 = 65
a2 = 572


m1 = 1021
m2 = 16381

min = 0
max = 1

x1 = 1
x2 = 13
n=10000 #number of random numbers to be generated
def f(x):
	return (1-x**2)**0.5

def random_number1(min, max):
	global x1
	x1 = a1* x1 % m1
	return min + (max-min)*x1/m1
def random_number2(min, max):
	global x2
	x2 = a2*x2%m2
	return min + (max-min)*x2/m2
#(a) throwing points between x = [0,1] and y = [0,1]
print("(a) By throwing points:")
count=0
for i in range (n):
	x=random_number1(min, max)
	y=random_number1(min, max)
	if f(x) >= y:
		count+=1
print("For a = 65 and m = 1021")		
print("The probability of a point inside the curve is: ", count/n)
print("The value of the integral is: ", (count/n)*(max-min)*(max-min))
print()

count=0
for i in range (n):
	x=random_number2(min, max)
	y=random_number2(min, max)
	if f(x) >= y:
		count+=1
print("For a = 572 and m = 16381")		
print("The probability of a point inside the curve is: ", count/n)
print("The value of the integral is: ", (count/n)*(max-min)*(max-min))
print()

print("(b) By solving the integral using Monte Carlo:")
print("For a = 65 and m = 1021")
sum=0
for i in range(n):
	x=random_number1(min, max)
	sum+=f(x)
print("The value of the integral is: ", sum/n)
print()
print("For a = 572 and m = 16318")
sum=0
for i in range(n):
	x=random_number2(min, max)
	sum+=f(x)
print("The value of the integral is: ", sum/n)
print("The value of pi/4 = ",m.pi/4)

"""
(a) By throwing points:
For a = 65 and m = 1021
The probability of a point inside the curve is:  0.8021 
The value of the integral is:  0.8021

For a = 572 and m = 16381
The probability of a point inside the curve is:  0.7865
The value of the integral is:  0.7865

(b) By solving the integral using Monte Carlo:
For a = 65 and m = 1021
The value of the integral is:  0.7853849536412534

For a = 572 and m = 16318
The value of the integral is:  0.785858307169474
The value of pi/4 =  0.7853981633974483
"""