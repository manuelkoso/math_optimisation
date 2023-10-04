Table of contents
<!-- TOC -->
* [0-1 Knapsack problem](#0-1-knapsack-problem)
* [Assignment problem](#assignment-problem)
* [Set covering problem](#set-covering-problem)
    * [First exercise](#first-exercise)
    * [Second exercise](#second-exercise)
* [Set packing problem](#set-packing-problem)
* [Set partitioning problem](#set-partitioning-problem)
<!-- TOC -->

# 0-1 Knapsack problem

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

# Assignment problem

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

# Set covering problem

### First exercise

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

### Second exercise

The director of a television channel for local information must
organise the work of the teams of journalists and operators to
cover m different off-site services. The editor-in-chief has prepared
n possible activities that a each individual team can carry out,
where an activity is the set of services that can be performed and
involves a certain cost of remuneration for the team, including
travel costs and any overtime hours. The director must decide
which of the activities to do in order to pay as little as possible
with the guarantee that each of the services is “covered” by at
least one team.

# Set packing problem

The famous shop window designer Ulivetto Laziali was called to set
up the shop window of the most important florist of Trieste. With
the m flowers, of different shape and colour, that the florist
provided him, Ulivetto produces n different sketches of floral
arrangements and for each of them also provides a score of
“compositional beauty”. He therefore decides to set up a set of
floral arrangements in the shop window that maximises the overall
score (defined as the sum of the scores of the individual
compositions created). The problem is clearly a packing problem
as it cannot create two compositions containing the same flower.

# Set partitioning problem

The manager of a construction site in Vicenza for the new
high-speed line must contract out m different works. The
procurement office has prepared several possible contract
assignments, each of which is made up of a subset of the works
which, for reasons of efficiency, it is good that they are performed
by the same company. For each contract assignment is also defined
the cost. The problem is to decide which contracts to award so
that all the works are carried out and the cost of the contracts is
minimum. This problem can easily be formulated as a partition
problem.