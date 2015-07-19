#Task 1
#we need tuple_sum([(1,2),(10,20)],[(3,4),(30,40)])---------------->[(4,6),(40,60)]
def tuple_sum(A,B):
	return [ (x+y for (x,y) in zip(a,b)) for (a,b) in zip(A,B) ]
#Task 2
def inv_dict(d):
	return {v:k for (k,v) in zip(d.keys(),d.values())}
##Alternative |----> def inv_dict(d):  return {v:k for (k,v) in d.items()} 
#Task 3
def row(p,n):
	return [ p + k for k in range(n+1) ]
##Alternative |----> def row(p,n):  return list(range(p,p+n))
#Task 4
Pr_f_is_even = 0.7
Pr_f_is_odd  = 0.3
#Task 5
Pr_g_is_1    =  0.4
Pr_g_is_0or2 = 0.6
