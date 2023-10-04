import gurobipy as gp
from gurobipy import GRB
import numpy as np


def assignment():
    model = gp.Model("assignment")

    x = model.addMVar((4, 4), vtype=GRB.BINARY)

    rows = range(4)
    columns = range(4)

    costs = np.array([[13, 4, 7, 6], [1, 11, 5, 4], [6, 7, 2, 8], [1, 3, 5, 9]])

    for i in rows:
        model.addConstr(gp.quicksum(x[i, j] for j in columns) <= 1)

    for j in columns:
        model.addConstr(gp.quicksum(x[i, j] for i in rows) == 1)

    model.setObjective(
        gp.quicksum(costs[i, j] * x[i, j] for j in columns for i in rows),
        GRB.MINIMIZE
    )

    model.optimize()

    print("\nSolution")
    for i in rows:
        for j in columns:
            if x[i, j].x == 1:  # to access the variable value
                print("Machine ", i, " is assigned to task ", j)


assignment()
