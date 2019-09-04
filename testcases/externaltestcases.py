import sys
sys.path.append('..')

import arithmetic

# https://stackoverflow.com/questions/6645357/doing-math-to-a-list-in-python
def tc1():
	return True
	
# https://stackoverflow.com/questions/16454107/math-operation-on-list-of-numbers
def tc2():
    pointA = [ 22, 44, 83 ]
    pointB = [ -17, 11, -25 ]
    pointC = [ 5, 55, 61 ] # output
    arithmetic.listsub(pointA,pointB) == pointC
    return True

# https://stackoverflow.com/questions/18713321/element-wise-addition-of-2-lists
def tc3():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    arithmetic.listsum(list1,list2) == [5, 7, 9]
    return True

# https://stackoverflow.com/questions/23173294/how-to-mathematically-subtract-two-lists-in-python?noredirect=1&lq=1
def tc4():
    A = [3, 4, 6, 7]
    B = [1, 3, 6, 3]
    arithmetic.listsub(A,B) == [2, 1, 0, 4]
    return True
	
# https://stackoverflow.com/questions/8194156/how-to-subtract-two-lists-in-python
def tc5():
    List1=[3,5,6]
    List2=[3,7,2]
    List3=[0,-2,4] # output
    arithmetic.listsub(List1,List2) == List3
    return True

def tc6():
    return True

# https://stackoverflow.com/questions/10271484/how-to-perform-element-wise-multiplication-of-two-lists
def tc7():
    a = [1,2,3,4]
    b = [2,3,4,5]
    assert arithmetic.listmul(a,b) == [2, 6, 12, 20]
    return True

# https://stackoverflow.com/questions/35166633/how-do-i-multiply-each-element-in-a-list-by-a-number/35166717
def tc8():
	return True

# https://stackoverflow.com/questions/55098623/product-of-every-element-of-two-linear-arrays?noredirect=1&lq=1
def tc9():
	x=[1, 4, 0 ,3]
	y=[2, 1, 9 ,4]
	z=[2, 4, 0, 12] # output
	assert arithmetic.listmul(x,y) == z
	return True



def main():
    print('Start tests')
    tc2()
    tc3()
    tc4()
    tc5()
    tc7()
    tc9()
    print('All test successfull')

if __name__== "__main__":
	main()