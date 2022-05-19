from matplotlib import mlab
import mm1
import math 
import matplotlib.pyplot as plt
n=1e6
mm1.seed = 1
a=572
m=16381
#determining the volume of steinmetz solid by Monte carlo method by intersection of two perpendicular cylinders each of radius 1 unit
count=0
arr=[[],[],[]]
for i in range(int(n)):
	x=-1+2*mm1.mlcg_random_number(a,m)
	y=-1+2*mm1.mlcg_random_number(a,m)
	z=-1+2*mm1.mlcg_random_number(a,m)
	if y**2+z**2<=1 and x**2+z**2<=1:
		count+=1
		#arr[0].append(x)
		#arr[1].append(y)
		#arr[2].append(z)
volume_of_cube=2**3
print("The volume of the steinmetz solid is : ",count/n*volume_of_cube)
#fig=plt.figure()
#ax=plt.axes(projection='3d')
#ax.plot3D(arr[0],arr[1],arr[2], '.')
#plt.show()

"""
-----------output---------------------------
The volume of the steinmetz solid is :  5.38032
"""