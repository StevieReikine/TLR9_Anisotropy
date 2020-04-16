import matplotlib.pyplot as plt
from scipy.optimize import fsolve, curve_fit
import random as rdm
import numpy as np

X1 = [x*0.1 for x in range(1, 10)]
X2 = list(range(1,101))
X = X1 + X2


data = np.loadtxt("mTLR9_1668_dataonly.txt")
#print(data)
data_x = data[:,0]
data_y = data[:,1]
#print(data_x, len(data_x), data_y, len(data_y))


def MyFuntion(X, K1, K4):
    SolutionFound = False
    Y = [0]*len(X)
    Af = 130
    Ab = 250
    i = 0
    for P0 in X:
        def equations(x):
            P, D, PD, P2D2 = x
            eq1 = P*D/PD - K1
            eq2 = PD*PD/P2D2 - K4
            eq3 = P + PD + 2*P2D2 - P0
            eq4 = D + PD + 2*P2D2 - D0
            return (eq1, eq2, eq3, eq4)
        #while not SolutionFound:
        for j in range(1000):
            P, D, PD, P2D2 = fsolve(equations, (rdm.uniform(0,P0),D0,rdm.randrange(0,D0),0.5),maxfev=50000)
            #P, D, PD, P2D2 = fsolve(equations, (rdm.randint(0,P0),rdm.randrange(0,D0),rdm.randrange(0,D0),rdm.randrange(0,D0)),maxfev=5000000)
            #print(P0)
            Ff = D/D0
            Fb = (PD + 2*P2D2)/D0
            F = Ff + Fb
            A = Af*Ff + Ab*Fb
            if(F>0.99 and F<1.01 and P>0 and D>0 and PD>0 and P2D2>0 and A > Af and A < Ab):
                    #print(Ff + Fb)
                    #print(equations((P, D, PD, PDD, PPD, P2D2, P2)))
                    SolutionFound = True
                    break
        Y[0] = Af
        #print(i)
        if i > 0:
            if SolutionFound:
                Y[i] = A
            else:
                Y[i] =Y[i-1]
        i = i + 1
    return(Y)

K1 = 7
K4 = 40
D0 = 5

Y = MyFuntion(data_x, K1, K4)

plt.plot(np.log10(data_x), data_y, 'b-', label= 'data')

popt, pcov = curve_fit(MyFuntion, data_x, data_y, p0 = [7.0, 50.0])
print(popt)

plt.plot(np.log10(data_x), Y, 'r-', label= 'fit')
plt.show()

Y = MyFuntion(data_x, popt[0], popt[1])

np.savetxt('Kd-test-K1-K4_fitted_e.csv', (data_x, Y), delimiter=',')