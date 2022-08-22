"""Come up with a function that divides the first input by the second input:"""
def division(divA,divB):
    return(divA/divB)
print(division(100,5))

"""Use the con function for the following question"""
def con(a, b):
    return(a + b)
"""Can the con function we defined before be used to add two integers or strings?"""
print(con(1, 1))
print(con('Si ', 'Funciona'))

"""Can the con function we defined before be used to concatenate lists or tuples?"""
print(con([1,2,3],[4,5,6]))
print(con(('a',1,True), ('b',2, False)))