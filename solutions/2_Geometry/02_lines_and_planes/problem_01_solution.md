### Exercise 1. Line Through Two Points
Find the equation of the line through $A=(1,2)$ and $B=(4,-1)$ in parametric and general form. Identify a direction vector and an example of a normal vector. Check that both points satisfy the equation you obtain.

> **Why this exercise:** teaches how to move between equivalent descriptions of a line and connect them with the appropriate vectors.

### Solution to Exercise 1. Line Through Two Points

Given two points:

$$
A=(1,2), \qquad B=(4,-1).
$$

**1. Direction vector**

A direction vector is obtained by subtracting the coordinates of the points:

$$
\vec{d}=\overrightarrow{AB}=B-A=(4-1,-1-2)=(3,-3).
$$

We can simplify it to:

$$
\vec{d}=(1,-1).
$$

**2. Parametric form**

The parametric equation of a line passing through $A=(x_0,y_0)$ with direction vector $\vec{d}=(a,b)$ is

$$
\begin{cases}
x=x_0+at,\\
y=y_0+bt,
\end{cases}
\qquad t\in\mathbb{R}.
$$

Substituting $A=(1,2)$ and $\vec{d}=(1,-1)$ gives

$$
\begin{cases}
x=1+t,\\
y=2-t,
\end{cases}
\qquad t\in\mathbb{R}.
$$

**3. General form**

The general equation of a line is

$$
Ax+By+C=0,
$$

where $(A,B)$ is a normal vector perpendicular to the line.

Since $\vec{d}=(1,-1)$, we can choose

$$
\vec{n}=(1,1),
$$

because

$$
\vec{d}\cdot\vec{n}=1\cdot 1+(-1)\cdot 1=0.
$$

Thus, the equation has the form

$$
x+y+C=0.
$$

Substituting the point $A=(1,2)$:

$$
1+2+C=0
\quad\Rightarrow\quad
C=-3.
$$

Therefore, the general equation is

$$
x+y-3=0.
$$

**4. Verification**

For $A=(1,2)$:

$$
1+2-3=0.
$$

For $B=(4,-1)$:

$$
4+(-1)-3=0.
$$

Both points satisfy the general equation.

We can also verify the parametric form:

- For $t=0$, we obtain $(x,y)=(1,2)=A$.
- For $t=3$, we obtain $(x,y)=(4,-1)=B$.

**Final answer**

- **Direction vector:** $\vec{d}=(1,-1)$.
- **Normal vector:** $\vec{n}=(1,1)$.
- **Parametric form:**

$$
\begin{cases}
x=1+t,\\
y=2-t,
\end{cases}
\qquad t\in\mathbb{R}.
$$

- **General form:**

$$
x+y-3=0.
$$

