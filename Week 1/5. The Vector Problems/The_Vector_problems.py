from GF2 import one
#one www.youtube.com/watch?v=jKwvmOR8Rj8 :)
#Task 1
p1_v = [-1, 3]
p1_u = [0, 4]
#define a vector addition function 
#(the addition by hand is much easier I will define a function just for practice)
def vec_add(v,w):  return [v[i]+w[i] for i in range(len(w))]
#Using the function 
p1_v_plus_u = [-1,7]
p1_v_minus_u = [-1,-1]
p1_three_v_minus_two_u = [-3,1]

#Task 2
p2_u = [-1,  1, 1]
p2_v = [ 2, -1, 5]
p2_v_plus_u = [1,0,6]
p2_v_minus_u = [3,-2,4]
p2_two_v_minus_u = [5,-3,9]
p2_v_plus_two_u = [0,1,7]

#Task 3
p3_vector_sum_1 = [one,0,0]
p3_vector_sum_2 = [0,one,one]

#Task 4
u_0010010 = { 'c' , 'd' ,'e'}
u_0100010 = {'b',' c' , 'd', 'e'}
##Ex. for  the first u_{0010010}
##'c' = |0|0|1|1|0|0|0|
##'d' = |0|0|0|1|1|0|0|       /\         /\
##'e' = |0|0|0|0|1|1|0|         -           -
##--------------------------------- /\--------
## +      0  0  1  0  0  1   0 -------\/--------    
#Task 5

v_0010010 =  {'c', 'd'}
v_0100010 = set()

#Task 6

x_gf2 = [one,0,0,0]

#Task 7

v1 = [2, 3, -4, 1]
v2 = [1, -5, 2, 0]
v3 = [4, 1, -1, -1]

#Task 8

uv_a = 5
uv_b = 6
uv_c = 16
uv_d = -1
