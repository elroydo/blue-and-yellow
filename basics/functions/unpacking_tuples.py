def main():
    x, y = 1, 2
    z = 3, 4, 5
    
    print(z, type(z))
    
    print(f'x={x} y={y}')
    tmp = x
    x = y
    y = tmp
    print(f'x={x} y={y}')
    x, y = y, x #woah
    print(f'x={x} y={y}')
    
    a, b, _ = 3, 6, 9 #underscore dummy var
    print(f'a={a} b={b} _={_}')
    c, d, *other = 10, 20, 30, 40 
    print(f'c={c} d={d} *other={other}')
    
    n1 = (1, 3, 5)
    n2 = (2, 4, 6)
    m = (n1, n2) #tuples tuples 
    print(m)
    n = (*n1, *n2) #merges tuples using star
    print(n)
    
    
main()