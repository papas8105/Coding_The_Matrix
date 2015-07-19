#Task 1
def myFilter( L , num):
	return [x for x in L if x % num != 0 ]
#Task 2
def my_lists(L):
	return [ list(range(1,x)) for x in L]
#what's the story mother? ta ta ta  my_lists([1,2,4]) ---> [[1], [1, 2], [1, 2, 3, 4]] >>> my_lists([0,3])--->[[], [1, 2, 3]]
#Task 3
def  myFunctionComposition(f, g):
	# f:A->B & g:B->C then fog:A->C here the domain and codomail are represented via dictionaries
        #>>> f = {0:'a',1:'b'}
        # >>> g = {'a':'apple','b':'banana'}
        #>>> myFunctionComposition(f,g) == {0:'apple',1:'banana'} 
        #edw theloume thn gof
        { k:g[f[k]] for k in f.keys()}
#Task 4
def mySum(L):
	s = 0
        #not allowed to use the built in "sum"
        for x in L:
        	s = s + x
        return s
#Task 5
def myProduct(L):
	p = 1
        for x in L:
        	p = p * x
        return p
#Task 6 not allowed to use "min" for the list
def myMin(L):
	m = float('infinity')
        for x in L:
        	m = min(x,m)
        return m
#Task 7
def myConcat(L):
	s = ""
        for x in L:
        	s = s + x
        return s
#Task 8
def myUnion(L):
	u = set()
        for x in L:
        	u = u.union(x)
        return u
#Task 9
complex_addition_a = 5 + 3j
complex_addition_b = 0 + 1j
complex_addition_c = -1 + 0.001j
complex_addition_d = 0.001 + 9j
#Task 10
def transform(a,b,L):
	return [a * x + b for x in L ]
#Task 11
GF2_sum_1 = 1 
GF2_sum_2 = 0
GF2_sum_3 = 0
#That's all folks!

