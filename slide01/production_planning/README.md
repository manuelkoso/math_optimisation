# Production planning

4 types of fertilisers whose processing is carried out by two departments

|                       | Type 1 | Type 2  | Type 3  | Type 4  |
|-----------------------|--------|---------|---------|---------|
| production department | 2  h   | 1.5  h  | 0.5   h | 2.5   h |
| packing department    | 0.5 h  | 0.25  h | 0.25 h  | 1   h   |

|        | Type 1 | Type 2 | Type 3 | Type 4 |
|--------|--------|--------|--------|--------|
| profit | 250    | 230    | 110    | 350    |

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
Note that this is not an integer linear problem. I'll do it later. 