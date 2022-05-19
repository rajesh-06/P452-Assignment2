import math as m
import matplotlib.pyplot as plt
import mm1
import numpy as np
import copy

A=mm1.readfile("assign2fit.txt",1)
A=mm1.transpose(A)
X,Y=A
sig=[1 for i in range(len(X))]

def phi0(x):
    return 1

def phi1(x):
    return 2*x-1

def phi2(x):
    return 8*x**2-8*x+1

def phi3(x):
    return 32*x**3-48*x**2+18*x-1

phi=[phi0, phi1, phi2, phi3]
y1=[]
y2=[]
b,chi2=mm1.poly_fit_chebyshev(X,Y,sig,phi)
b1,chi=mm1.poly_fit(X,Y,sig,3)
print("Fitting coefficients in polynomial fitting:",b1)
print()
print("Fitting coefficients in Chebyshev basis:",b)

"""

plt.plot(X,Y,'ro-',label="data")
plt.plot(X,mm1.chebyshev_value(X,phi,b),'b-',label="fit_chebyshev")
plt.plot(X,mm1.poly_value(X,b1),'g-',label="fit_poly")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.legend()
plt.show()
"""


#----------output-------------
"""
Fitting coefficients in polynomial fitting: [0.5746586674196096, 4.7258614421419285, -11.128217777643231, 7.66867762290941]

Fitting coefficients in Chebyshev basis: [1.1609694790335525, 0.39351446798815237, 0.046849832090106576, 0.23964617571596983]

"""