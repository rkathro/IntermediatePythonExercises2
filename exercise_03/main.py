import numpy as np

def main():
    #Create list of random floats
    randomNums = np.random.rand(10)

    #Print list of values
    print("Random numbers: " + str(randomNums))

    #Print Mean, Median, and Standard Deviation
    print("Mean: " + str(np.mean(randomNums)) + ", Median: " + str(np.median(randomNums)) + ", Standard Deviation: " + str(np.std(randomNums)))
    
main()