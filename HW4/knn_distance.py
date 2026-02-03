def knn_distance(arr, q, k):
    # partition
    pivot = abs(arr[-1] - q)
    i = 0
    for j in range(0, len(arr) - 1):
        if abs(arr[j] - q) <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    
    arr[i], arr[-1] = arr[-1], arr[i]
    print(arr)
    #check order
    if i+1 == k:
        return ((abs(arr[i] - q), arr[i]))
    elif i+1 > k:
        return knn_distance(arr[:i], q, k)
    elif i+1 < k:
        return knn_distance(arr[i+1:], q, k - i-1)
        
