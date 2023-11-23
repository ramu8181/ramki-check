import numpy as np
m,n = map(int, input().split())
list1 = []
for _ in range (0,m):
    list1.append(list(map(int,input().split())))
list1 = np.array(list1)
print (np.prod(np.sum(list1,axis=0)))
#list1 = np.array([input().split() for i in range (0,m) ] ,int)
#list1 = np.array(list1)
#print (np.prod(np.sum(list1,axis=0)))
