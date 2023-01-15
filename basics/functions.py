import datetime

def main():
    desires = brazil('Bob')
    print(desires)
    
def brazil(who):
    age = input(f'Hola {who}, how old are you?\n')
    birth = tahiti(age)
    return input(f'What would a person born in {birth} want?\n')
    
def tahiti(age):
    now = datetime.datetime.now().year
    return now - int(age)

#where is this leading to?

def keyword():
    plums = input('How many plums?\n')
    #positionless positioned parameter arguments; oh yea
    cost = plum(price=0.3, quantity=int(plums))
    
    print(f'Total cost £{cost}')
    
def plum(quantity, price):
    return quantity * price

main()
keyword()