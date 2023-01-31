def main():
    a = [1, 2, 3, 4, 5, 6]
    
    #different ways to square numbers in a
    print(list(square(a))) #function
    print(list(map(lambda n: n**3, a)))
    print([n**4 for n in a])
    
    print(list(filter(lambda n: n > 3, a)))
    
    print([n for n in a if n > 4])
    
    #comprehensions are cool
    
def square(list):
    squares = []
    for item in list:
        squares.append(item**2)
        
    return squares
    
main()