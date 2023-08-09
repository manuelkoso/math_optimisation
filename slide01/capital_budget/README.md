# Capital budget

We have to invest 1000$ on the financial market. The market offers three different types of investments,
each characterized by a purchase price and a net yield. 

|                | A   | B   | C   |
|----------------|-----|-----|-----|
| Purchase price | 750 | 200 | 800 |
| Yield          | 20  | 5   | 10  |

So, we want to maximise the return. A, B, and C cannot be carried out in a partial 
way. 

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
So, this is an ansignment problem. 
