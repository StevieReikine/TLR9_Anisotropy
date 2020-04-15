import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import random as rdm
import numpy as np

def equations(x):
    P, D, PD1, PD2, PDD = x
    eq1 = P*D/PD1 - K1
    eq2 = P*D/PD2 - K2
    eq3 = P*D*D/(K1*K2) - PDD
    eq4 = P + PD1 + PD2 + PDD - P0
    eq5 = D + PD1 + PD2 + 2*PDD - D0
    return (eq1, eq2, eq3, eq4, eq5)

K1 = 20
K2 = 40
D0 = 2
X = []
Y = []
for P0 in range (0,20,1):
    for i in range(10000):
        P, D, PD1, PD2, PDD = fsolve(equations, (rdm.randint(0,P0),1,0.5,rdm.randrange(0,D0),0.5),maxfev=50000)
        #P, D, PD, PDD, PPD, P2D2, P2 = fsolve(equations,(P0,D0,D0,D0,D0,D0,5),maxfev=50000)
        #print(P0)
        Ff = D/D0
        Fb = (PD1 + PD2 + 2*PDD)/D0
        F = Ff + Fb
        if(F>0.999999999999 and F<1.00000000001):
        #if(P>0 and D>0 and PD>0 and PDD>0 and PPD>0 and P2D2>0 and P2>0):
                print(Ff + Fb)
                #print(equations((P, D, PD, PDD, PPD, P2D2, P2)))
                break
    Af = 58.8
    Ab = 186.1
    A = Af*Ff + Ab*Fb
    print(A)
    X.append(P0)
    Y.append(A)

for P0 in range (20,100,10):
    for i in range(10000):
        P, D, PD1, PD2, PDD = fsolve(equations, (rdm.randint(0,P0),1,0.5,rdm.randrange(0,D0),0.5),maxfev=50000)
        #P, D, PD, PDD, PPD, P2D2, P2 = fsolve(equations,(P0,D0,D0,D0,D0,D0,5),maxfev=50000)
        #print(P0)
        Ff = D/D0
        Fb = (PD1 + PD2 + 2*PDD)/D0
        F = Ff + Fb
        if(F>0.999999999999 and F<1.00000000001):
        #if(P>0 and D>0 and PD>0 and PDD>0 and PPD>0 and P2D2>0 and P2>0):
                print(Ff + Fb)
                #print(equations((P, D, PD, PDD, PPD, P2D2, P2)))
                break
    Af = 58.8
    Ab = 186.1
    A = Af*Ff + Ab*Fb
    print(A)
    X.append(P0)
    Y.append(A)

plt.scatter(X,Y)
plt.show()

np.savetxt('Kd-test-20-40_b.csv', (X, Y), delimiter=',')
