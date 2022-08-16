def pairs(arr,length):
    count = 0
    arr.sort()
    print(arr)
    i = 0
    while(i<length-1):
        if arr[i]==arr[i+1]:
            count += 1 
            i += 2
        else:
            i += 1    
    print(count)        
arr = [1,1,2,1,2,3,5,21,23,32,3,4,5,2]
length = len(arr)
pairs(arr,length)