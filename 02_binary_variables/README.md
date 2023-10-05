Table of contents
<!-- TOC -->
* [0-1 Knapsack problem](#0-1-knapsack-problem)
* [Assignment problem](#assignment-problem)
* [Set covering problem](#set-covering-problem)
<!-- TOC -->

# [0-1 Knapsack problem](knapsack.py)

Suppose you are planning a
picnic. You’ve constructed a list
of items you would like to carry
with you on the picnic. Each
item has a weight associated
with it and your knapsack is
limited to carrying no more than
15 pounds. You have also come
up with a 1 to 10 rating for each
item, which indicates how
strongly you want to include the
particular item in the knapsack
for the picnic. This information
is listed in the next table.

| Item          | Weight | Rating |
|---------------|--------|--------|
| Ant repellent | 1      | 2      |
| Beer          | 3      | 9      |
| Blanket       | 4      | 3      |
| Bratwurst     | 3      | 8      |
| Brownies      | 3      | 10     |
| Frisbee       | 1      | 6      |
| Salad         | 5      | 4      |
| Watermelon    | 10     | 10     |

# [Assignment problem](assignment.py)

A company has 4 machines available for assignment to 4 tasks.
Any machine can be assigned to any task, and each task requires
processing by one machine. The time required to set up each
machine for the processing of each task is given in the table below.

|           | Task 1 | Task 2 | Task 3 | Task 4 |
|-----------|--------|--------|--------|--------|
| Machine 1 | 13     | 4      | 7      | 6      |
| Machine 2 | 1      | 11     | 5      | 4      |
| Machine 3 | 6      | 7      | 2      | 8      |
| Machine 4 | 1      | 3      | 5      | 9      |

The company wants to minimise the total setup time needed for
the processing of all four tasks.

# [Set covering problem](set_covering.py)

A typical application concerns facility location. Suppose we are
given a set of potential sites N = {1, . . . , n} for the location of
fire stations. A station placed at j costs cj.

We are also given a set
of communities M = {1, . . . , m} that have to be protected. The
subset of communities that can be protected from a station
located at j is Mj.

For example, Mj might be the set of
communities that can be reached from j in 10 minutes. Then the
problem of choosing a minimum-cost set of locations for the fire
stations such that each community can be reached from some fire
station in 10 minutes is a set-covering problem.

Let M = {1, 2, 3, 4, 5},
{M} = {{1, 3, 5}, {2, 3}, {1, 4}, {3, 4, 5}, {2}, {5}, {1, 5}},
c = [3, 5, 1, 9, 2, 4, 1].