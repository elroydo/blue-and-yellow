#no constants for you!

def main():
    something = input('How many teeth?\n')
    print(something)
    
    avocados = input('How many avocados?\n')
    carbon_print = int(avocados) * 0.19
    
    print(f'You\'re killing the planet by eating {avocados} avocados at {carbon_print}kg of Co2 equivalents!')
    #all that jazz of floats, booleans, and strings
    print(float(avocados), bool(avocados))
    
main()