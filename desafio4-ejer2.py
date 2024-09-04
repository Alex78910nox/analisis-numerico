A=0.15
e=0.90
T=650
eA=0.01
ee=0.01
eT=40
cont=5.67*10**-8
H=A*e*cont*T**4
dA=e*cont*T**4
de=A*cont*T**4
dT=A*e*cont*4*T**3
error=dA*eA+de*ee+dT*eT
print(H)
print(error)
print("mas error: ",H+error)
print("menos erro: ",H-error)