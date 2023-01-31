from random import randint

def main():
    people = [{'name': 'John', 'age': 111},
              {'name': 'Jane', 'age': 222},
              {'name': 'Bob', 'age': 333}]
    
    name = input('Enter a name: ')
    
    #for else
    for person in people:
        p = person['name']
        if p.lower() == name.lower():
            print(person)
            break
    else:
        print(f'{name} not found.')
    
    fruits = [{'fruit': 'Apple', 'qnt': 33},
              {'fruit': 'Banana', 'qnt': 22},
              {'fruit': 'Cherry', 'qnt': 333}]
    
    fruit = input('Enter a fruit: ').lower()
    print(fruit)
    
    i = 0
    
    #while else
    while i < len(fruits):
        store  = fruits[i]
        if store['fruit'].lower() == fruit:
            print(f"{store['qnt']} {store['fruit']}(s) in stock.")
            break
        i += 1
    else:
        qnt = int(input(f'Enter how many {fruit}(s) you would like: '))
        fruits.append({'fruit': fruit, 'qnt': qnt})
        print(fruits)
        
    #do while doens't exist in python...
    #substitute with while and if condition to break
    MIN = 0
    MAX = 10
    ent = randint(MIN, MAX)
    x = 0
    
    print(f'Guess my number, between {MIN} and {MAX}')
    
    while True:
        x += 1
        
        guess = int(input(' > '))
        
        if guess > ent:
            print("Smaller!")
        if guess < ent:
            print("Bigger!")
        else:
            print(f"Bingo! It only took {x} goes...")
            break
    
main()