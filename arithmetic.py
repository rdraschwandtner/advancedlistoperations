import operator

# See ./experiments/experiment-map-vs-list-comp-vs-lambda-list-comp.ipynb
# https://stackoverflow.com/a/57615641/11963667
def element_wise_lstcompfct(lhs, rhs, f):
    return [element_wise_lstcompfct(i, j, f) if type(i) == list and type(j) == list else f(i, j) for i, j in zip(lhs, rhs)]


def listsum(lhs, rhs):
    return element_wise_lstcompfct(lhs, rhs, operator.add)

def listsub(lhs, rhs):
    return element_wise_lstcompfct(lhs, rhs, operator.sub)

def listmul(lhs, rhs):
    return element_wise_lstcompfct(lhs, rhs, operator.mul)

def listdiv(lhs, rhs):
    return element_wise_lstcompfct(lhs, rhs, operator.truediv)




def main():
	# sum
	a = [1,2,3,4,[5,6,7,8]]
	b = [10,20,30,40,[50,60,70,80]]
	c = listsum(a,b)
	c
    
    
	e = [1,2,3,4,[5,6,7,8]]
	listsum(e, e)
	
	f = [1,[2,3], 4, [5,6,7], [[8], [9,10]]]
	g = [10,[20,30], 40, [50,60,70], [[80], [90,100]]]
	listsum(f, g)
    
	listsub(e, e)
	listsub(f, g)
	listsub(g, f)
    
	listmul(e,e)
	listmul(f, g)
    
	listdiv(e,e)
	listdiv(f, g) 

	# negative tests
	h = [1,2,3,4,[5,'a',7,8]]
	try:
		listsum(h, h) # should raise exception
	except Exception as error:
		print(error)
		pass
    
	try:
		listsum(e, h) # should raise exception
	except Exception as error:
		print(error)
		pass
    
	i = [1,2,3,4,[5,0,7,8]]    
	try:
		listsum(e, i) # should raise exception
	except Exception as error:
		print(error)
		pass
    
    
if __name__== "__main__":
	main()