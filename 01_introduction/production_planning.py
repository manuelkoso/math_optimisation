import gurobipy as gp
from gurobipy import GRB


def production_planning():
    try:
        model = gp.Model("production_planning")

        # 4 variables
        x_1 = model.addVar(vtype=GRB.CONTINUOUS, name="x_1")
        x_2 = model.addVar(vtype=GRB.CONTINUOUS, name="x_2")
        x_3 = model.addVar(vtype=GRB.CONTINUOUS, name="x_3")
        x_4 = model.addVar(vtype=GRB.CONTINUOUS, name="x_4")

        model.setObjective(250 * x_1 + 230 * x_2 + 110 * x_3 + 350 * x_4, GRB.MAXIMIZE)

        model.addConstr(2 * x_1 + 1.5 * x_2 + 0.5 * x_3 + x_4 * 2.5 <= 100, "c0")
        model.addConstr(0.5 * x_1 + 0.25 * x_2 + 0.25 * x_3 + x_4 * 1 <= 50, "c1")

        model.optimize()

        for v in model.getVars():
            print('% s % g ' % (v.VarName, v.X))
        print(' Obj : % g ' % model.ObjVal)

    except gp.GurobiError as e:
        print(' Error code ' + str(e.errno) + ': ' + str(e))
    except AttributeError:
        print(' Encountered an attribute error ')


production_planning()