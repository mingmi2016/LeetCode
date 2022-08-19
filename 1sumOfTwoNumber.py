import numpy as np


arr = input("please input int array:")
num = [int(n) for n in arr.split()]
intss = np.array(num)

targets = input("please input target:")
target = int(targets)

listReturn = []
for i in range(len(intss)):
    for j in range(len(intss)-1):
        if intss[i] + intss[j+1] == target:
           listReturn.append(i)
           listReturn.append(j+1)
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




