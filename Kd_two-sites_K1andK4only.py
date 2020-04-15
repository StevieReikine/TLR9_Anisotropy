import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import random as rdm
import numpy as np

def equations(x):
    P, D, PD, P2D2 = x
    eq1 = P*D/PD - K1
    eq2 = PD*PD/P2D2 -K4
    eq3 = P + PD + 2*P2D2 - P0
    eq4 = D + PD + 2*P2D2 - D0
    return (eq1, eq2, eq3, eq4)


X1 = list(range(0,20))
X2 = list(range(20,110, 10))
X = X1 + X2
Y = [0]*len(X)

def MyFuntion(P0, X, Y):
    SolutionFound = False
    for i in range(100):
        P, D, PD, P2D2 = fsolve(equations, (rdm.randint(0,P0),rdm.randrange(0,D0),rdm.randrange(0,D0),rdm.randrange(0,D0)),maxfev=50000)
        #P, D, PD, PDD, PPD, P2D2, P2 = fsolve(equations,(P0,D0,D0,D0,D0,D0,5),maxfev=50000)
        #print(P0)
        Ff = D/D0
        Fb = (PD + 2*P2D2)/D0
        F = Ff + Fb
        if(F>0.999999999999 and F<1.00000000001 and P>0 and D>0 and PD>0 and P2D2>0):
        #if(P>0 and D>0 and PD>0 and PDD>0 and PPD>0 and P2D2>0 and P2>0):
                print(Ff + Fb)
                #print(equations((P, D, PD, PDD, PPD, P2D2, P2)))
                SolutionFound = True
                break
    Af = 180
    Ab = 250
    A = Af*Ff + Ab*Fb
    print(A, P, D, PD, P2D2)
    X.append(P0)
    Y.append(A)

K1 = 20
K4 = 40
D0 = 5
X = []
Y = []

for P0 in range (0,20,1):
    MyFuntion(P0, X, Y)

for P0 in range (20,100,10):
    MyFuntion(P0, X, Y)

plt.scatter(X,Y)
plt.show()

np.savetxt('Kd-test-K1-K4_b.csv', (X, Y), delimiter=',')