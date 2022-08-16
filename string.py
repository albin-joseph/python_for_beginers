def array(arr,a,b):
    flag = -1
    res = len(arr)
    for i in range(0,res):
        if arr[i] == a or arr[i] == b:
            if flag!=-1 and arr[i]!=arr[flag]:
                res = min(res,i-flag)
            flag = i 
             
    if res == len(arr):
        return 1
    else:
        print(res)
              
arr = ["apple","orange","banana","grapes","banana","banana","apple","apple","blueberry","apple","orange","avacado","kiwi","apple","orange","pear"]
a = "pear"
b = "kiwi"
#length = len(arr)
print("Distance length between ",a,",",b, ": " )
array(arr,a,b)