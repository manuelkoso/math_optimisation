import gurobipy as gp
from gurobipy import GRB

from Exercise import Exercise


class CapitalBudget(Exercise):

    def solve_exercise(self):
        try:
            model = gp.Model("cap_budget")

            # variables
            x_1 = model.addVar(vtype=GRB.BINARY, name="x_1")
            x_2 = model.addVar(vtype=GRB.BINARY, name="x_2")
            x_3 = model.addVar(vtype=GRB.BINARY, name="x_3")

            # objective function
            model.setObjective(20 * x_1 + 2 * x_2 + 10 * x_3, GRB.MAXIMIZE)

            # constraints
            model.addConstr(750 * x_1 + 200 * x_2 + 800 * x_3 <= 1000, "c0")

            # optimise
            model.optimize()

            # print result
            for v in model.getVars():
                print('% s % g ' % (v.VarName, v.X))
            print(' Obj : % g ' % model.ObjVal)

        except gp.GurobiError as e:
            print(' Error code ' + str(e.errno) + ': ' + str(e))
        except AttributeError:
            print(' Encountered an attribute error ')
