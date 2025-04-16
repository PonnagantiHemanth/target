def fun(matrix):
    reslt = []
    reslt += matrix.pop(0)
    for i in matrix:
        reslt += [i.pop()]
    if matrix:
        reslt += matrix.pop()[::-1]
    print(reslt)
    print(matrix)
matrix = [
    [1, 2, 3,9],
    [4, 5, 6,90],
    [7, 8, 9,23],
    [1,2,3,4,5]
]
v = fun(matrix)