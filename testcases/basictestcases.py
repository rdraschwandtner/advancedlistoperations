import sys
sys.path.append('..')

import arithmetic


def tc1():
	a = [1,2,3,4]
	b = [5,6,7,8]
	assert arithmetic.listsum(a,b) == [6, 8, 10,12]
	assert arithmetic.listsub(a,b) == [4, -4, -4,-4]    
	return True

def tc2():
	a = [[1,2],[3,4]]
	b = [[5,6],[7,8]]
	assert arithmetic.listsum(a,b) == [[6, 8], [10,12]]
	assert arithmetic.listsub(a,b) == [[4, -4], [-4,-4]]  
	return True

def tc3():
	a = [1,2,3,4,[5,6,7,8]]
	assert arithmetic.listsum(a,a) == [2,4,6,8,[10,12,14,16]]
	return True

def tc4():
	a = [1,[2,3], 4, [5,6,7], [[8], [9,10]]]
	b = [10,[20,30], 40, [50,60,70], [[80], [90,100]]]
	assert arithmetic.listsum(a,b) ==  [11,[22,33], 44, [55,66,77], [[88], [99,110]]]
	return True

def tc5():
	a = [1,[2,3], 4, [5,6,7], [[8], [9,10]]]
	b = [10,[20,30], 40, [50,60,70], [[80], [90,100]]]
	assert arithmetic.listmul(a,b) ==  [10, [40, 90], 160, [250, 360, 490], [[640], [810, 1000]]]
	assert arithmetic.listmul(a,a) ==  [1, [4, 9], 16, [25, 36, 49], [[64], [81, 100]]]
	assert arithmetic.listdiv(a,b) ==  [0.1, [0.1, 0.1], 0.1, [0.1, 0.1, 0.1], [[0.1], [0.1, 0.1]]]
	assert arithmetic.listdiv(a,a) ==  [1.0, [1.0, 1.0], 1.0, [1.0, 1.0, 1.0], [[1.0], [1.0, 1.0]]]
	return True

def main():
    print('Start tests')
    tc1()
    tc2()
    tc3()
    tc4()
    tc5()
    print('All test successfull')

if __name__== "__main__":
	main()
