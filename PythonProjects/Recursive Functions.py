def Fibonacci(n): # Recursive Function created.
    if(n <= 1): # If n smaller than 1 returned 1
        return 1
    else: # Else n * (n-1)
        return (n * Fibonacci(n-1))
    
n = Fibonacci(int(input("Write number of fibonacci : ")))
print(n)