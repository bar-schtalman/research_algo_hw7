import numpy
import numpy as np
import cvxpy as cp
import time
import matplotlib.pyplot as plt
"""
this is implementation of solving linear equations systems using numpy and cvxpy
with the test function "check_np_cp(n)" n is the number of linear systems it will solve
and display a graph to compare both methods runtime
"""


def np_solve(n):
    t1 = time.time()
    for i in range(2,n):
        l = np.random.randint(1,5000,(i,i))
        r = np.random.randint(1,5000,(i,1))
        np.linalg.solve(l,r)
    t2 = time.time() - t1
    return t2


def cp_solve(n):
    t1 = time.time()
    for i in range(2,n+1):
        x = cp.Variable(i)
        objective = cp.Minimize(0)
        constraints = []
        l = np.random.randint(1, 5000, (i, i))
        r = np.random.randint(1, 5000, (i, 1))
        for j in range(i):
            constraints.append(x[j] * l[j,j] == r[j])
        prob = cp.Problem(objective,constraints)
        prob.solve()
    t2 = time.time() - t1
    return t2


def check_np_cp(n):
    np_times = []
    cp_times = []
    n_values = []
    for i in range(2,n):
        n_values.append(i)
        np_times.append(np_solve(i))
        cp_times.append(cp_solve(i))
    plt.plot(n_values,np_times, label='numpy')
    plt.plot(n_values,cp_times, label='cvxpy')
    plt.xlabel('n')
    plt.ylabel('time')
    plt.legend()
    plt.show()


check_np_cp(100)






