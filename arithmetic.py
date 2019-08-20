import operator
import functools
import numbers

def my_listsum_wrapper(lhs, rhs, op):
    # bind operator-function to function call. Functions are not iterable, so map() would throw an error.
    return list(map(functools.partial(my_listsum,op=op), lhs, rhs)) # https://stackoverflow.com/questions/10314859/applying-map-for-partial-argument
    
def my_listsum(lhs, rhs, op):
    if isinstance(lhs, list) == True:
        return my_listsum_wrapper(lhs, rhs, op)
    elif (isinstance(lhs, numbers.Number) & isinstance(rhs, numbers.Number)): 
        return op(lhs, rhs) # lhs and rhs are scalars
    else:
        raise Exception('Structure not OK. lhs: ' + str(lhs) + ' rhs: ' + str(rhs))


def my_arbitrarylistsum(lhs, rhs):
    return my_listsum_wrapper(lhs, rhs, operator.add)


def main():
	e = [1,2,3,4,[5,6,7,8]]
	my_arbitrarylistsum(e, e)
	
	f = [1,[2,3], 4, [5,6,7], [[8], [9,10]]]
	g = [10,[20,30], 40, [50,60,70], [[80], [90,100]]]
	my_arbitrarylistsum(f, g)

    # negative tests
    h = [1,2,3,4,[5,'a',7,8]]
    try:
        my_arbitrarylistsum(h, h) # should raise exception
    except Exception as error:
        print(error)
        pass
    
    try:
        my_arbitrarylistsum(e, h) # should raise exception
    except Exception as error:
        print(error)
        pass
    
if __name__== "__main__":
	main()