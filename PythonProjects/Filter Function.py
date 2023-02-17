def IsPrimeNumber(n): # Filter Function created.
    if(n > 100): # If n bigger than 100 returned False
        print(f"This system is supported only smaller than 100 of numbers. Entered value : {n}")
        return False
    # Else user_value != n and user_value % n == 0 -> this n values are 2,3,5,7 because these are prime numbers.  
    if((n % 2 == 0 and n != 2) or
       (n % 3 == 0 and n != 3) or
       (n % 5 == 0 and n != 5) or
       (n % 7 == 0 and n != 7)):
        return True
    return False

numbers = [11,1221,300,5,2,15,9,100,21,4] # Numbers for filter function
print(list(filter(IsPrimeNumber,numbers))) # Filtered and printed.