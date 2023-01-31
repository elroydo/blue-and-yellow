from functools import reduce

def main():
    add = [10, 20, 30, 40, 50, 60]
    
    
    totalSum = reduce(sum, add)
    print(totalSum)
    
    #efficient
    totalRed = reduce(lambda a, b: a + b, add)
    print(totalRed)
    
    
def sum(a, b):
    return a + b
    
main()