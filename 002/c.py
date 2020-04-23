#O(n) without using division 
array = [1,2,3,4,5]
n = len(array)
#print(array)

n_array = [1 for i in range(n)]
aux = 1
for i in range(n):
    n_array[i] = aux
    aux *= array[i]

aux = 1
for i in range(len(array)-1, -1, -1):
    n_array[i] = aux*n_array[i]
    aux *= array[i]

print(n_array)