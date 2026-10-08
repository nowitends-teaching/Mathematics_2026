### Exercise 7. Linear Dependence Without Heavy Computation

Given

$$
u=(1,2,3),\qquad v=(2,4,6),\qquad w=(0,1,1).
$$

Identify a specific relation between $u$ and $v$, decide whether the three vectors can be linearly independent, and explain why no long calculation is needed.

> **Why this exercise:** develops the habit of recognizing structure before applying a computational procedure.

## Solution

Coordinate comparison immediately shows

$$
v=2u,
$$

or equivalently $2u-v+0w=0$. This is a nontrivial linear relation, so the set $\{u,v,w\}$ is linearly dependent regardless of $w$.

No determinant or row reduction is needed: two proportional vectors already supply a dependence relation for the whole set.
