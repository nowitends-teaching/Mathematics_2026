### Exercise 6. Projection and Perpendicular Component

Find the projection of $u=(4,2)$ onto the direction $v=(1,1)$. Then compute

$$
r=u-\mathrm{proj}_v\,u
$$

and verify that $r\cdot v=0$. Explain this result geometrically.

> **Why this exercise:** shows projection as a decomposition into parallel and perpendicular components.

## Solution

Using the projection formula,

$$
\mathrm{proj}_v\,u=\frac{u\cdot v}{v\cdot v}v=\frac{6}{2}(1,1)=(3,3).
$$

Thus

$$
r=u-\mathrm{proj}_v\,u=(4,2)-(3,3)=(1,-1),
$$

and the requested calculation is

$$
r\cdot v=(1,-1)\cdot(1,1)=1-1=0.
$$

The projection $(3,3)$ is parallel to $v$, so it is the component of $u$ in the projection direction. Subtracting this parallel component leaves the perpendicular component $r$. The zero dot product verifies geometrically that $r$ is perpendicular to the direction $v$.
