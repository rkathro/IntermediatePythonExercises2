import time
import random

# Fibonacci function
def fibonacci(x):
    a, b = 0, 1
    for y in range(2, x + 1):
        a, b = b, a + b
    return b

def main():
    #Create random value between 15 and 35 inclusive
    randomValue = random.randint(15, 35)

    #Get start time
    start = time.time()

    #Calculate Fibonacci Value
    fibonacciValue = fibonacci(randomValue)

    #Get end time
    end = time.time()

    #Calculate time spent
    totalTime = end - start

    #Print results
    print("fib(" + str(randomValue) + ") = " + str(fibonacciValue))
    print("fib(" + str(randomValue) + ") took " + str(totalTime) + " seconds")
main()