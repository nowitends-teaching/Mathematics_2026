### Exercise 12. A Normal Vector to a Plane

Given $A=(1,0,2)$, $B=(2,1,0)$, and $C=(0,3,1)$. Construct two vectors lying in the plane, find a vector perpendicular to both, and check the perpendicularity using dot products.

> **Why this exercise:** creates a direct bridge from vectors to the description of a plane.

## Solution

Two vectors in the plane are

$$
\overrightarrow{AB}=(1,1,-2),\qquad \overrightarrow{AC}=(-1,3,-1).
$$

Their cross product is

$$
\overrightarrow{AB}\times\overrightarrow{AC}=(5,3,4).
$$

The nonzero cross product shows that the two in-plane vectors are not parallel, so the three points determine a plane. Thus $n=(5,3,4)$ is a normal vector to the plane through the three points.

The requested dot-product checks are

$$
n\cdot\overrightarrow{AB}=5+3-8=0,
$$

$$
n\cdot\overrightarrow{AC}=-5+9-4=0.
$$

Both in-plane directions are perpendicular to $n$, which verifies that $n$ is a normal vector.
