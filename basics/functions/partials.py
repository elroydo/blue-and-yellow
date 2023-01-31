from functools import partial

def main():
    x = 3
    f = partial(multiply, x)
    
    res = f(11)
    print(res)
    
def multiply(a, b):
    return a*b
    
main()