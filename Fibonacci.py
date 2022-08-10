def fibonacci(a):
    p = sum = 0
    q = 1
    print ("The Fibonacci Series is:")
    if (a == 0):
        print ("Nothing to print")
        return
    elif (a == 1):
        print (str(p) + "\t" + "")
        return
    elif (a == 2):
        print (str(p) + "\t" + str(q) + "")
        return    
    else:
        print (str(p) + "\t" + str(q) + "\t", end = " ")
        for i in range (a - 2):
            sum = p + q
            print (str(sum) + "\t" , end = " "),
            p = q
            q = sum            

a = int(input("Enter a number: "))
fibonacci(a)