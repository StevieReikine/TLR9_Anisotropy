import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import random as rdm
import numpy as np

# this function simulates what the Anisotropy would be for a value of P0, Ka, and Kb
def Anisotropy(X, K_a, K_b):
    # variable to test whether a solution to the set of equations was found (to be used after fsolve)
    SolutionFound = False
    # set up parameters of system
    Y = [0]*len(X)
    Af = 58.8
    Ab = 186.1
    i = 0
    for P0 in X:
        def equations(x):
            P, D, PD1, PD2, PDD = x
            eq1 = P*D/PD1 - K_a
            eq2 = P*D/PD2 - K_b
            eq3 = P*D*D/(K_a*K_b) - PDD
            eq4 = P + PD1 + PD2 + PDD - P0
            eq5 = D + PD1 + PD2 + 2*PDD - D0
            return (eq1, eq2, eq3, eq4, eq5)
        for j in range(100):
                P, D, PD1, PD2, PDD = fsolve(equations, (rdm.randint(0,P0),1,0.5,rdm.randrange(0,D0),0.5),maxfev=50000)
                Ff = D/D0                       # definition of Fraction Free D
                Fb = (PD1 + PD2 + 2*PDD)/D0     # definition of Fraction Bound D
                F = Ff + Fb                     # F must be 1
                A = Af*Ff + Ab*Fb               # Definition of Anisotropy
                # check that solutions found meet physical constrains, e.g. F = 1, no negative values, and Af < A < Ab                
                if(F>0.9999 and F<1.0001 and P>0 and D>0 and PD1>0 and PD2>0 and PDD>0 and A > Af and A < Ab):
                    SolutionFound = True
                    break
        Y[0] = Af       # by definition, so do not update Y[0] based on fit generated above
        if i > 0:   
            # update Y = A if conditions met
            if SolutionFound:
                Y[i] = A
            # in case a solution is not found, update Y with previous value of A- this is not ideal but it generates a value of A for every P0 and for most values of P0, Y will be close
            else:
                Y[i] = Y[i-1]
        i = i + 1
    return(Y)                                       

# set desired values of Ka and Kb to simulate
K_a = 20
K_b = 40

# set value of D0
D0 = 2

# set range of x values: 0 to 20 in steps of 1 then 20 to 100 in steps of 10
X1 = list(range(0,20))
X2 = list(range(20,101, 10))
X = X1 + X2

# simulate anisotropy data for given X, Ka, and Kb    
Y = Anisotropy(X, K_a, K_b)

# plot the data
plt.scatter(X,Y)
plt.show()

# save the simulated data as a vs file
np.savetxt('Kd-test-20-40_d.csv', (X, Y), delimiter=',')
