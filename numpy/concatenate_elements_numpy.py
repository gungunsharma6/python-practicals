# To concatenate element wise two arrays of string
import numpy as np
e=int(input('enter the size of the array'))
for m in range(1,3):
    c=[]
    d=[]
    print('enter elements of',m,'array')
    for f in range(e):
        g=input('enter the element:')
        c.append(g)
    for h in range(e):
        k=input("enter the element:")
        d.append(k)
    c=np.array(c)
    d=np.array(d)
    if(m==1):
        l=np.array([c,d])
        print(l)
    elif(m==2):
        n=np.array([c,d])
        print(n)
new_array=np.char.add(n,l)
print(new_array)