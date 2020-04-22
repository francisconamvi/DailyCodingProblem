#O(n*log(n))
n = int(input())
array = list(map(int, input().split()))
k = int(input())

array.sort() #merge sort n log n
for i in range(n):
    # busca binaria de k-array[i]
    if(k-array[i] in array):
        print(array[i], k-array[i], "True")
        quit()

print("False")