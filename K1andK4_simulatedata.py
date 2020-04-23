import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import random as rdm
import numpy as np

# Set values for X, first 0-1 in steps of 0.1 then up to 100 in steps of 1
X1 = [x*0.1 for x in range(1, 10)]
X2 = list(range(1,101))
X = X1 + X2

# this function simulates what the Anisotropy would be for a value of P0, K1, and K4
def Anisotropy(X, K1, K4):
    # variable to test whether a solution to the set of equations was found (to be used after fsolve)
    SolutionFound = False
    # set up parameters of system
    Y = [0]*len(X)      # generate list of Y values, initiallized to 0
    Af = 130            # Free Anisotropy (this is empirical- set to match data)
    Ab = 250            # Bound Anisotropy (this is empirical- set to match data)
    i = 0
    for P0 in X:
        # define the set of equations that governs the interaction being modeled 
        def equations(x):
            P, D, PD, P2D2 = x
            eq1 = P*D/PD - K1               # K1 = [P]*[D]/[PD]
            eq2 = PD*PD/P2D2 - K4           # K4 = [PD]^2/[P2D2]
            eq3 = P + PD + 2*P2D2 - P0      # P0 = P + PD + 2*P2D2   (conservation of mass)
            eq4 = D + PD + 2*P2D2 - D0      # D0 = D + PD + 2*P2D2   (conservation of mass)
            return (eq1, eq2, eq3, eq4)
        for j in range(100):
            # solve the equation to get values of P, D, PD, and P2D2 
            # it is useful to chose physically reasonable initial values: e.g. P must be between 0 and P0
            P, D, PD, P2D2 = fsolve(equations, (rdm.uniform(0,P0),D0,rdm.randrange(0,D0),0.5),maxfev=50000)
            Ff = D/D0                   # definition of Fraction Free D
            Fb = (PD + 2*P2D2)/D0       # definition of Fraction Bound D
            F = Ff + Fb                 # F must be 1
            A = Af*Ff + Ab*Fb           # Definition of Anisotropy
            # check that solutions found meet physical constrains, e.g. F = 1, no negative values, and Af < A < Ab
            if(F>0.99 and F<1.01 and P>0 and D>0 and PD>0 and P2D2>0 and A > Af and A < Ab):
                    SolutionFound = True
                    break
        Y[0] = Af   # by definition, so do not update Y[0] based on fit generated above
        if i > 0:
            # update Y = A if conditions met
            if SolutionFound:
                Y[i] = A
            # in case a solution is not found, update Y with previous value of A- this is not ideal but it generates a value of A for every P0 and for most values of P0, Y will be close
            else:
                Y[i] =Y[i-1]
        i = i + 1
    return(Y)

# set values for K1 and K4
K1 = 7
K4 = 2

# value for D0
D0 = 5

# simulate Anisotropy data for desired range of X and given K1, K4
Y = Anisotropy(X, K1, K4)

# plot the data
plt.scatter(X,Y)
plt.show()

# save the simulated data in a sv file
np.savetxt('Kd-test-K1-K4_c.csv', (X, Y), delimiter=',')
