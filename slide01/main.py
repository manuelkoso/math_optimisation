import capital_budget as cb
import production_planning as pp


def main():
    problem = input("Select a problem to execute: \n"
                    "1 - capital budget\n"
                    "2 - production planning\n")
    if int(problem) == 1:
        cb.capital_budget()
    elif int(problem) == 2:
        pp.production_planning()


if __name__ == "__main__":
    main()
