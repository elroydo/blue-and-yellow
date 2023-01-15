def main():
    memories = 'Like tears in rain.'
    memento = "I can't remember to forget you."
    house = '"Never better."'
    walker = 'Walker walks a lot when he\'s drinking'
    
    mind = r'C:\python\bin'
    #fishing for minds
    
    print(memories, memento, house, walker, mind)
    #bulking!
    
    lines = '''
    dots:
        .
        .
        dot
    '''
    print(lines)
    #many lines and dots
    
    name = 'unknown'
    screen = 'Hi ' f'{name}'
    universe = '.'
    print(screen + universe)
    #concatenating things
    print(screen[-7])
    #negative indexing...
    print(len(screen))
    #how long the long
    print(screen[6:9])
    #like sushi
    new_screen = 'Bye' + screen[2:]
    print(new_screen + universe)
    #etching regrets
    
main()