def main():
    #range; start, stop, step...
    for index in range(0, 33, 3):
        if(index % 2):
            continue #skips iteration
        print(index)
        
    #sums of sums of sums
    sum = 0
    for val in range(33):
        sum += val
    print(sum)
    
    #while it never ends!
    counter = 0
    while counter < 3:
        print(counter)
        counter+= 1

    command = ''
    while command.lower() != 'quit': #lowercase
        command = input('> ')
        if(command.lower() == 'break'):
            break
        print(f'echo: {command}')
        
def fun():
    pass #something to procrastinate about later...
        
main()
fun()
#hm