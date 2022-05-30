# to capitalize the first letter of all the elements of a given array
import numpy as np
a=['python','c++','c','java','gla']
a=np.array(a)
print('original array: ',a)
cap_array=np.char.capitalize(a)
print('new array: ',cap_array)