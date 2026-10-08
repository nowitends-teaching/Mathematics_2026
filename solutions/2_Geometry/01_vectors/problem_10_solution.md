### Exercise 10. Triangle Area from Vectors

The points $A=(0,0,0)$, $B=(2,1,0)$, and $C=(1,3,2)$ form a triangle. Construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$, compute the area of the parallelogram using the cross product, and then find the area of the triangle. Explain the factor $\frac12$.

> **Why this exercise:** shows the interpretation of the length of the cross product as area.

## Solution

### Essential formulas and theory

A vector from one point to another is found by subtracting coordinates: $\overrightarrow{AB}=B-A$. For $u=(u_1,u_2,u_3)$ and $v=(v_1,v_2,v_3)$,

$$
u\times v=(u_2v_3-u_3v_2,\;u_3v_1-u_1v_3,\;u_1v_2-u_2v_1),\qquad
\|u\|=\sqrt{u_1^2+u_2^2+u_3^2}.
$$

The cross-product length equals base times height, so it gives the parallelogram area. A diagonal divides the parallelogram into two congruent triangles; therefore,

$$
S_{\mathrm{parallelogram}}=\|u\times v\|,\qquad
S_{\mathrm{triangle}}=\frac12\|u\times v\|.
$$

### Step 1. Construct the side vectors

$$
\begin{aligned}
u=\overrightarrow{AB}&=(2-0,1-0,0-0)=(2,1,0), \\
v=\overrightarrow{AC}&=(1-0,3-0,2-0)=(1,3,2).
\end{aligned}
$$

### Step 2. Compute the cross product

$$
\begin{aligned}
u\times v&=(1\cdot2-0\cdot3,\;0\cdot1-2\cdot2,\;2\cdot3-1\cdot1) \\
&=(2-0,\;0-4,\;6-1)=(2,-4,5).
\end{aligned}
$$

### Step 3. Find both areas

$$
S_{\mathrm{parallelogram}}
=\sqrt{2^2+(-4)^2+5^2}
=\sqrt{4+16+25}=\sqrt{45}=3\sqrt5.
$$

Taking half gives the triangle area:

$$
S_{\mathrm{triangle}}=\frac12\,3\sqrt5=\frac{3\sqrt5}{2}.
$$
