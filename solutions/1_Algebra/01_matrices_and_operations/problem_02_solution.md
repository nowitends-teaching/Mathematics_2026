### Exercise 1. Determinant of a 2×2 Matrix
Compute

$$
\det
\begin{pmatrix}
3 & -2 \\
5 & 4 \\
\end{pmatrix},\qquad \det
\begin{pmatrix}
1 & 7 \\
2 & 14 \\
\end{pmatrix}.
$$

Which matrix is invertible? Justify your answer.

> **Why this exercise:** introduces the simplest determinant calculation and immediately connects it with invertibility.

### Solution: Exercise 1. Determinant of a 2×2 Matrix

For a $2\times2$ matrix,

$$
\det\begin{pmatrix}a & b\\ c & d\end{pmatrix}=ad-bc.
$$

Therefore,

$$
\det\begin{pmatrix}3 & -2\\ 5 & 4\end{pmatrix}
=3\cdot4-(-2)\cdot5=12+10=22,
$$

and

$$
\det\begin{pmatrix}1 & 7\\ 2 & 14\end{pmatrix}
=1\cdot14-7\cdot2=14-14=0.
$$

A square matrix is invertible exactly when its determinant is nonzero. Thus, the first matrix is invertible because its determinant is $22$, while the second matrix is not invertible because its determinant is $0$.