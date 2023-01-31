def main():
    args()
    
    res = add(1, 2, 3, 4, 5, 6)
    print(res)
    
    print(tot(3, 4, 6, 8, 7, z=9))
    
    a = (0, 1)
    print(*a)
    
def add(a, b, *args):
    x = a + b
    for arg in args:
        x += arg
    return x

def args(*args): #star cool
    print(args)
    print(type(args)) #a tuple!
    
def tot(*args, z):
    return sum(args) + z

def point(x, y):
    return f'({x},{y})'
    
main()