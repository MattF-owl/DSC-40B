import random


def knn_distance(arr, q, k):
    def quickselect(left, right, k):
        #choose pivot
        idx = random.randint(left, right)
        pivot = abs(arr[idx] - q)
        arr[idx], arr[-1] = arr[-1], arr[idx]

        #partition
        i = left
        for j in range(left, right ):
            if abs(arr[j] - q) <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i+=1
        
        arr[i], arr[-1] = arr[-1], arr[i]
        if i+1 == k:
            return ((abs(arr[i] - q), arr[i]))
        elif i+1 > k:
            return quickselect(left, i, k)
        elif i+1 < k:
            return quickselect(i+1, right, k)
    return quickselect(0, len(arr) - 1, k)

        
