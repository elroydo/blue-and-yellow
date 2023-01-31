def main():
    nums = [3, 2, 1]
    
    #iterator = map(double, nums)
    iterator = map(lambda num: num*2, nums)
    
    print(nums, "\n", list(iterator))
    
    
def double(val):
    return val*2
    
main()