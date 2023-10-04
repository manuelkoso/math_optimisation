import gurobipy as gp
from gurobipy import GRB


def knapsack():
    model = gp.Model("knapsack")

    x = model.addVars(8, vtype=GRB.BINARY)
    model.setObjective(
        2 * x[0] + 9 * x[1] + 3 * x[2] + 8 * x[3] + 10 * x[4] + 6 * x[5] + 4 * x[6] + 10 * x[7],
        GRB.MAXIMIZE)

    model.addConstr(1 * x[0] + 3 * x[1] + 4 * x[2] + 3 * x[3] + 3 * x[4] + 1 * x[5] + 5 * x[6] + 10 * x[7] <= 15, "c0")

    model.optimize()

    # print result
    for v in model.getVars():
        print('% s % g ' % (v.VarName, v.X))
    print(' Obj : % g ' % model.ObjVal)


knapsack()
