# to repeat all elements three times of a given array of string
import numpy as np
a=eval(input('enter the list :'))
a=np.array(a)
print(a)
new_array=np.char.multiply(a,3)
print(new_array)