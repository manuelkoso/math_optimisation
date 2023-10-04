Table of contents
<!-- TOC -->
* [Production planning](#production-planning)
* [Capital budget](#capital-budget)
<!-- TOC -->

# Production planning

A chemical industry manufactures 4 types of fertilisers, Type 1, Type 2, Type 3, and
Type 4, whose processing is carried out by two departments of the industry: the
production department and the packaging department. In order to obtain ready-to-sell
fertiliser, processing in both departments is necessary. The following table shows, for
each type of fertiliser, the times (in hours) necessary for processing in each of the
departments to have a ton of fertiliser ready for sale.

|                       | Type 1 | Type 2  | Type 3  | Type 4  |
|-----------------------|--------|---------|---------|---------|
| production department | 2  h   | 1.5  h  | 0.5   h | 2.5   h |
| packing department    | 0.5 h  | 0.25  h | 0.25 h  | 1   h   |

After deducting the cost of the raw material, each tonne of fertiliser gives the
following profits (prices expressed in euros per tonne)

|        | Type 1 | Type 2 | Type 3 | Type 4 |
|--------|--------|--------|--------|--------|
| profit | 250    | 230    | 110    | 350    |

Determine the quantities that must be produced weekly of each type of fertiliser in
order to maximise the overall profit, knowing that every week, the production
department and the packaging department have a maximum working capacity of 100
and 50 hours, respectively.

The objective function is defined as follows:

```math
max(f(x)) = max(250x_1 + 230x_2 + 110x_3 + 350x_4)
```

where the constraints are:

```math
x_i \in \mathbb{R} , where \space i \in \{ 1,2,3,4 \}
```
```math
x_i \geq 0 , where \space i \in \{ 1,2,3,4 \}
```
```math
2x_1 + 1.5x_2 + 0.5x_3 + 2.5x_4 \leq 100
```
```math
0.5x_1 + 0.25x_2 + 0.25x_3 + 1x_4 \leq 50
```

# Capital budget

Suppose we have to invest e1000 on the financial market. We also
assume that the market offers three different types of investments
(A, B, C), each characterised by a purchase price and a net yield,
which are summarised in the following table:

|                | A   | B   | C   |
|----------------|-----|-----|-----|
| Purchase price | 750 | 200 | 800 |
| Yield          | 20  | 5   | 10  |

You want to decide which of the investments to make to maximise
the return, knowing that investments A, B, C cannot be carried
out in a partial way, i.e., they are not divisible.

The objective function is defined as follows:

```math
max(20x_1 + 2x_2 + 10x_3)
```
and the constraints are:

```math
x_i \in \{0,1\}, \space \text{where} \space i \in \{1,2,3\}
```
```math
750x_1 + 200x_2 + 800x_3 \leq 1000
```