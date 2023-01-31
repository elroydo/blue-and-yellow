def main():
    majors = ['d', 'e', 'g', 'a', 'b']
    list_loops(majors)
    print()
    indexing(majors)
    print()
    iterables()
    
def list_loops(list):
    #looping
    for major in list:
        print(major)
        
    #tuple with indexes
    for major in enumerate(list):
        print(major)
    #unpacked
    for index, major in enumerate(list, 1):
        print(f"{index}: {major}")
        
def indexing(list):
    #indexing
    major = input("please enter a character:\n")
    
    if major in list:
        ind = list.index(major)
        print(f"index of 'a' is: {ind}")
    else:
        print(f"{major} doesn't exist")
        
def iterables():
    for index in range(3):
        print(index)
        
    str = 'Clouds'
    for ch in str:
        print(ch)
    
    print()
    
    #iterating over an iterator
    nums = [0, 1, 2]
    iterator = iter(nums)
    
    for num in iterator:
        print(num)
        
    #consuming iterators till exception
    nums = [0, 1, 2]
    iterator = iter(nums)
    print(next(iterator), next(iterator), next(iterator), next(iterator))
    
    
main()