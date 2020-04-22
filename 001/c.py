#O(n*log(n))
#implementing functions

def mergeSort(array):
    if len(array) > 1:
        m = len(array)//2

        l_array = array[:m]
        r_array = array[m:]
        
        mergeSort(l_array)
        mergeSort(r_array)

        i = 0
        j = 0
        k = 0

        while i<len(l_array) and j<len(r_array):
            if l_array[i] < r_array[j]:
                array[k] = l_array[i]
                i+=1
            else:
                array[k] = r_array[j]
                j+=1
            k+=1
        
        while i<len(l_array):
            array[k] = l_array[i]
            i+=1
            k+=1
        
        while j<len(r_array):
            array[k] = r_array[j]
            j+=1
            k+=1

def buscaBin(array, n):
    if(len(array)==0):
        return False
    m = len(array)//2
    if(array[m] == n):
        return True
    elif array[m] > n:
        return buscaBin(array[:m],n)
    else:
        return buscaBin(array[m+1:],n)

n = int(input())
array = list(map(int, input().split()))
k = int(input())

mergeSort(array)

for i in range(n):
    if(buscaBin(array,k-array[i])):
        print(array[i], k-array[i], "True")
        quit()

print("False")
