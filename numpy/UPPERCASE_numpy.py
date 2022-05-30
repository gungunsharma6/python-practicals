# to uppercase each element of the given array
import numpy as np
a=['python','c++','c','java','gla']
a=np.array(a)
print('original array: ',a)
upper_array=np.char.upper(a)
print('new array: ',upper_array)