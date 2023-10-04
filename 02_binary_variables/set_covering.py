import gurobipy as gb
from gurobipy import GRB
import numpy as np


def set_covering():
    model = gb.Model("set_covering")

    costs = np.array([3, 5, 1, 9, 2, 4, 1])

    A = np.array([[1, 0, 1, 0, 0, 0, 1],
                  [0, 1, 0, 0, 1, 0, 0],
                  [1, 1, 0, 1, 0, 0, 0],
                  [0, 0, 1, 1, 0, 0, 0],
                  [1, 0, 0, 1, 0, 1, 1]])

    b = np.ones(5)

    x = model.addMVar(7,
                      vtype=gb.GRB.BINARY)  # this allows mat operations, very similar (amd related) to np.arrays

    model.addConstr(A @ x >= b)
    model.setObjective(costs @ x)

    model.optimize()
    print(
        model.status)  # https://www.gurobi.com/documentation/9.5/refman/optimization_status_codes.html for all codes

    print("optimal" if model.status == 2 else ("infeasible" if model.status == 3 else (
        "unbounded" if model.status == 5 else "check the link page for other status codes")))

    print("\n\n", x.x, type(x), type(x.x))


set_covering()
