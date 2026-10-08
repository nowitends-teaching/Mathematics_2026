### Exercise 13. Do Four Points Lie in One Plane?

Given

$$
A=(0,0,0),\qquad B=(1,2,0),\qquad C=(0,1,1),\qquad D=(2,5,1).
$$

1. Construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$.
2. Find $n=\overrightarrow{AB}\times\overrightarrow{AC}$.
3. Construct $\overrightarrow{AD}$ and check whether $\overrightarrow{AD}\cdot n=0$.
4. Based on this, decide whether $D$ lies in the plane determined by $A,B,C$, and justify the criterion.

> **Why this exercise:** combines the known cross and dot products into a geometric criterion needed for planes, without introducing a separate concept used only once.

## Solution

The in-plane candidates are

$$
\overrightarrow{AB}=(1,2,0),\qquad \overrightarrow{AC}=(0,1,1).
$$

Their cross product is

$$
n=\overrightarrow{AB}\times\overrightarrow{AC}=(2,-1,1).
$$

Also $\overrightarrow{AD}=(2,5,1)$. The dot product is

$$
\overrightarrow{AD}\cdot n=2\cdot2+5(-1)+1\cdot1=4-5+1=0.
$$

Since $n\neq0$, the points $A,B,C$ determine a plane with normal $n$. Since this dot product is zero, $\overrightarrow{AD}$ is perpendicular to the normal, so $D$ lies in the plane through $A,B,C$. A vector lies in the plane parallel to $AB$ and $AC$ if and only if it is perpendicular to their nonzero normal. Thus $\overrightarrow{AD}\cdot n=0$ is both necessary and sufficient for $D$ to lie in the plane through $A$. All four points are coplanar.
