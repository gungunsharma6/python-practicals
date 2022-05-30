# to titlecase each element of the given array
import numpy as np
a=['pYtHon','C++','c','JavA','gLa']
a=np.array(a)
print('original array: ',a)
title_array=np.char.title(a)
print('new array: ',title_array)