# Loosy Compression algorithm
This is an application of the notions of linear algebra learnt through the first chapter of deeplearningbook such as:
-Scalars, vectors, matrices
-Types of matrices: diagonal, orthogonal, singular, identity
-Norms: Lp, L-infinity, Frobenius norl, Euclidean(L2) norm
-Eigen decomposition of matrices into vectors
-SIngular value decomposition of matrices
-Trace operators

# Practical example
We will write a loosy compression algorithm that will enable us compress set of vectors {x(1), x(2), x(3), x(4), ... , x(m)} belonging to Rn(real number vectors of n elemnts) to {c(1), c(2), c(3), c(4), ... , c(m)} belonging to Rl with l<n.
This algorithm will help in the efficient storage of original data from x-vectors to the c-vectors that occupy less space and that conserve the original data.
To do this we need to write two functions: <the encoding> and the <decoding> functions established from linear algebra.

# Encoding function
f(x)=c
Obtained by finding the optimal value of c: such that the distance between c and x will be minimal.
It is given by f(x)=D(T).c
where D(T) is the transpose of D
# Decoding function
it is that which enables us to get back to an approximate equal original data such that: x = g(f(x))
It is given by: g(f(x)) = D.D(T).x
Hence: g(c) = Dc
# Obtaining D
D is a matrix of l eigen vectors corresponding to the largest l eigen values of the matrix X.X(T)

# Algorithm steps
- Generating m vectors of length n. The set of vectors will constitute the matrix X.
- Computing XX(T) and finding its l largest eigen values
- Finding the corresponding l eigen vectors and building the D matrix
- Encoding: Computing the compressed data: for all x calculate c= D(T).x
- Decoding: Reverting the compressed data to the original data by using the decoded function: for all c ccalculate x=D(c)
- Evaluating the error using the distances between the vectors 
