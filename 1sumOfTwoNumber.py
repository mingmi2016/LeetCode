import numpy as np


arr = input("please input int array:")
num = [int(n) for n in arr.split()]
intss = np.array(num)

targets = input("please input target:")
target = int(targets)

listReturn = []
for i in range(len(intss)):
    for j in range(i+1,len(intss)):
        if intss[i] + intss[j] == target:
           listReturn.append(i)
           listReturn.append(j)
           break
    if len(listReturn) > 0:
        break

if len(listReturn) > 0:
    print('int array')
    print(intss)
    print('target:'+str(target))
    print(listReturn)
else:
    print('have not found the two number!')




