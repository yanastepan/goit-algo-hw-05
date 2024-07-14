from typing import Callable


# creating a function which returns inner function fibonacci(n)
# fibonacci (n) calculates the nth Fibonacci number.
# if the number is already in the cache, the function must return a value from the cache.
# if the number is not in the cache, the function must calculate it, save it to the cache, and return the result.
def caching_fibonacci() -> Callable[[int], int]:

    # initialize the cache as a dictionary
    cache = {}

    # creating an inner fibonacci function which takes n as an argument.
    # n is the order number of the Fibonacci number
    def fibonacci(n: int) -> int:
        
        if n in cache:          # checking if n is already in dictionary cache
            return cache[n]     # return value of the n key, if so
        
        if n == 0:              # return 0, if n is 0
            result = 0
        elif n == 1:            # return 1, if n is 1
            result = 1
        else:                   # recursive computation with caching
            result = fibonacci(n - 1) + fibonacci(n - 2)
        
        cache[n] = result       # store the computed value in the cache
        return result
                
              
    return fibonacci

# example of usage:
"""
fib = caching_fibonacci()

print(fib(15))
"""