#O(n)

n = int(input())
array = list(map(int, input().split()))
k = int(input())

seen = set()
for i in range(n):
    if k-array[i] in seen:
        print(array[i], k-array[i], "True")
        quit()
    seen.add(array[i])

print("False")
