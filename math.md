# 数学笔记
## strang circulant preconditioner
$A_n = [a_{j,k}]_{0<=j,k<=n-1} = [a_{j-k}]_{0<=j,k<=n-1}$ 是 toeplitz 矩阵,  
则 strang circulant preconditioner 矩阵为:  

$$
[S_n]_{k,0} = \left\{
\begin{aligned}
& a_k \\
& a_{n-k}
\end{aligned}
\right
$$