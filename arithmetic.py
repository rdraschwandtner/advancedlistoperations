import operator
import functools

def my_listsum_wrapper(lhs, rhs, op):
    # bind operator-function to function call. Functions are not iterable, so map() would throw an error.
    return list(map(functools.partial(my_listsum,op=op), lhs, rhs)) # https://stackoverflow.com/questions/10314859/applying-map-for-partial-argument
    
def my_listsum(lhs, rhs, op):
    if isinstance(lhs, list) == True:
        return my_listsum_wrapper(lhs, rhs, op)
    else: # lhs and rhs are scalars
        return op(lhs, rhs)


def my_arbitrarylistsum(lhs, rhs):
    return my_listsum_wrapper(lhs, rhs, operator.add)


def main():
	e = [1,2,3,4,[5,6,7,8]]
	my_arbitrarylistsum(e, e)
	
	f = [1,[2,3], 4, [5,6,7], [[8], [9,10]]]
	g = [10,[20,30], 40, [50,60,70], [[80], [90,100]]]
	my_arbitrarylistsum(f, g)


if __name__== "__main__":
	main()