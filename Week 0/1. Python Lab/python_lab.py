#Task 1
minutes_in_week = 7 * 24 * 60
#Task 2
remainder_without_mod = 2304811 - 47 * ( 2304811 // 47 )
#Task 3
divisible_by_3 = sum([673,909]) / 3 == 0
#Task 4
x = - 9 ; y = 1 / 2 ;
expression_val = 1 #2**(y+1/2) if x + 10 < 0 else 2 ** (y-1/2)
#Task 5
first_five_squares = {x ** 2 for x in {1,2,3,4,5}}
#Task 6
first_five_pows_of_two = {2 ** x for x in {0,1,2,3,4}}
#Task 7 (9 elements)
X1 = { 1, 2, 3 };Y1 = { 1, 5, 6 };
#Task 8 (5 elements)
X2 = { 1, -2, 4 };Y2 = { 0, -4, 2 };
#Task 9 (intersection without using '&')
S = {1, 2, 3, 4};T = {3, 4, 5, 6};
S_intersect_T = {x for x in S for y in T if x == y}
#Task 10
list_of_numbers = [20, 10, 15, 75];list_average = sum(list_of_numbers)/len(list_of_numbers);
#Task 11
cartesian_product = [ [x ,y ] for x in ['A','B','C'] for y in [1,2,3]]
#Task 12
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
LofL_sum = sum([sum(x) for x in LOfL] )
#Task 13
S = {-4, -2, 1, 2, 5, 0}
zero_sum = [ (x,y,z) for x in S for y in S for z in S if x + y +z == 0 ]
#Task 14
exclude_zero_list = zero_sum.remove((0,0,0))
#Task 15
first_of_tuples_list = exclude_zero_list[0]
#Task 16
example_L = [1,2,2]
#Task 17
odd_num_list_range = list(range(1,100,2))
#Task 18
L = ['A','B','C','D','E']
range_and_zip = list(zip(list(range(5)),L))
#Task 19
A = [10, 25, 40];B = [1, 15, 20];
list_sum_zip = [ x + y for ( x , y ) in zip(A,B)]
#Task 20
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = [ x[k] for x in dlist ]
#Task 21
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
value_list_modified_1 = [ x[k] if k in x else 'NOT PRESENT' for x in dlist]
#Task 22
square_dict = { k  : k ** 2 for k in range(0,100) }
#Task 23
D = {'red','white','blue'}
identity_dict = {x:x for x in D}
#Task 24
base = 10
digits = set(range(base))
representation_dict = {(base ** 2)*x + base * y + z : [x , y , z] for x in digits for y in digits for z in digits }
#Task 25
d = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
listdict2dict = {names[i]:d[i] if i in d else 0.0 for i in range(len(names))}
#Task 26
def nextInts(L): return [x + 1 for x in L]
#Task 27
def cubes(L): return [x ** 3 for x in L]
#Task 28
def dect2list(dct , keylist): return [ dct[k] for k in keylist ]
#Task 29
def list2dict(L,keylist): return {k:v for (k,v) in zip(keylist,L)}  
