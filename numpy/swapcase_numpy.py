# to swapcase each elements of the given array
import numpy as np
a=['pYtHon','C++','c','JavA','gLa']
a=np.array(a)
print('original array: ',a)
swapcase_array=np.char.swapcase(a)
print('new array: ',swapcase_array)