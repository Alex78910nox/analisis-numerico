import math
A=4*math.pi*(0.15**2)
e=0.90
T=550
eA=0.01
ee=0.05
eT=20
cont=5.67*10**-8
H=A*e*cont*T**4
dA=e*cont*T**4
de=A*cont*T**4
dT=A*e*cont*4*T**3
error=dA*eA+de*ee+dT*eT
print("H es: ",H)
print("error es: ",error)
print("mas error: ",H+error)
print("menos erro: ",H-error)