#O(n) using division
array = [1,2,3,4,5]
n = len(array)

mult = 1
for i in range(n):
    mult = mult * array[i]

n_array = list()
for i in range(n):
    n_array.append(mult//array[i])

print(n_array)