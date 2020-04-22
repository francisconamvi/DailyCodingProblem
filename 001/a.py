#O(n^2)
n = int(input())
array = list(map(int, input().split()))
k = int(input())

for i in range(n):
    for j in range(i+1,n):
        if(array[i]+array[j]==k):
            print(array[i], array[j], "True")
            quit()

print("False")