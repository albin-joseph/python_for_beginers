
def array_sum(arr,length,sum):
    low = 0
    high = length - 1
    while(low<high):
            if(arr[low] + arr[high] == sum):
                print("(",arr[low],",",arr[high],")", sep=" ")
            if(arr[low] + arr[high] > sum):
                high -= 2
            else:
                low += 1

a = [3, 5, 1, 2, 2, 5, 2, 2]  
arr = sorted(list(a))
print(arr)
length = len(arr)
sum = int(input("Enter the sum : "))      
print("The  pairs are :")
array_sum(arr,length,sum)