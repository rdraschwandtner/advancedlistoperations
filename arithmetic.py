
is_list = lambda e: isinstance(e,list)

def my_listsum(lhs, rhs):
    if is_list(lhs) == True:
        return list(map(my_listsum,lhs,rhs))
    else: # lhs and rhs are scalars
        return lhs + rhs

def my_arbitrarylistsum(lhs, rhs):
    return list(map(my_listsum,lhs,rhs))

def main():
	e = [1,2,3,4,[5,6,7,8]]
	my_arbitrarylistsum(e, e)
	
	f = [1,[2,3], 4, [5,6,7], [[8], [9,10]]]
	g = [10,[20,30], 40, [50,60,70], [[80], [90,100]]]
	my_arbitrarylistsum(f, g)


if __name__== "__main__":
	main()