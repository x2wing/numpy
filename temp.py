import numpy as np
from pprint import pprint
massive = ["X.O","XXX","XOO"]
# for i in massive:
#     for j in i:
# string = ''.join(massive)
    
a = np.array(list(''.join(massive)), str).reshape(3,3)
for i in range(len(massive)):
    print(a[i][1:], a[i][:-1])












# def foo(A,B):
#     if A > B: return A+1


# A = ["abc",
#      "def",
#      "ghi"]
# i=0
# for item in A:
#     print(item[~i])
#     i+=1
# foo(5,6)

