import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    mat = ''
    for i in matrix:
        for j in i:
            mat += str(j) + '  '
        mat += '\n'
    print(mat)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
# 4x4 by 4xn
def matrix_mult( m1, m2 ):
    m = len(m1)
    n = len(m2[0])
    m2_copy = [[m2[i][j] for j in range(n)] for i in range(4)]
    for i in range(m):
        for j in range(n):
            m2[i][j] = dot(m1[i], [m2_copy[k][j] for k in range(4)])

def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m

def dot(v1, v2):
    n = len(v1)
    s = 0
    for i in range(n):
        s += v1[i] * v2[i]
    return s