
#way to format and embed variables and expressions
def main():
    name = input('What\'s your name?\n')
    morning(name)
    when = input(f'When are you, {name}?\n')
    why(name, when)
    
    raw()
    backslash()
    
    
def morning(id):
    print(f'Bon Giorno {id}!')
    
def why(id, n):
    print(f'How may {n}s can there be in {{{{{{{id}}}}}}}?')
    
def raw():
    s = 'one\two\three'
    print(s)
    
    #as literal characters
    #best for paths
    a = r'one\two\three'
    print(a)
    
def backslash():
    print('Is \t anything \t real?\nMaybe.')
    
    colours = ['red','green','blue']
    rgb = '\n'.join(colours)
    s = f"rgb:\n{rgb}"
    print(s)
    
#nonsense...
main()