#O(n^2) without using division 
array = [1,2,3,4,5]
n = len(array)

n_array = [1 for i in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            n_array[j] = n_array[j] * array[i]
print(n_array)

