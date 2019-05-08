import numpy as np

# 1 sr = 4.25 x 10^10 arcsec^2
def sr_to_mas2(theta):
    arcsec2 = theta*4.25*10e10
    mas2= arcsec2*pow(1000, 2)
    return mas2

def ang_diam(area):
    return 2*np.sqrt(area/np.pi)

#in AU, radius = theta[mas] / p [mas], theta is angular radius
#215 solar radii in 1 au


#star 1:
p1 = .73 #mas
T1 = 5000
A1 = sr_to_mas2(1.4e-20)
print("A1: ", A1)
D1 = ang_diam(A1)
print("diam 1: ", D1)
r1 = (D1/2)/p1 * 215
print("radius 1: ", r1)

#star 2:
p2 = 130.2
T2 = 10000
A2 = sr_to_mas2(2e-16)
print("A2: ", A2)
D2 = ang_diam(A2)
print("diam 2: ", D2)
r2 = (D2/2)/p2 * 215
print("radius 2: ", r2)

#star 3:
p3 = 11.3
T3 = 6500
A3 = sr_to_mas2(2e-19)
print("A3: ", A3)
D3 = ang_diam(A3)
print("diam 3: ", D3)
r3 = (D3/2)/p3 * 215
print("radius 3: ", r3)
