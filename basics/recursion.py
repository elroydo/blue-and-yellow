def fn(count):
    print(count)
    if count > 0:
        fn(count-1)
    
fn(3)

def sum(n):
    return n + sum(n-1) if n > 0 else 0
    '''
    if n > 0:
        return n + sum(n - 1)
    return 0
    '''

val = input('Enter a number to sum:\n')
result = sum(int(val))
print(result)

#recursion... things within things of themselves