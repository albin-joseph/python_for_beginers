def factorial(n):
    if n == 1:
        return 1

    else:
        return(n*factorial(n-1))

number = int(input("Enter the number to find factorial: "))            
fact = factorial(number)
print("factorial of",number,"is",fact)    
