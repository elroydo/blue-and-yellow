import bottle #module
import bottle as calc #new name
from bottle import aloe_vera, ficus #fns
from bottle import ficus as div #fn with new name
from bottle import * #import all

def main():
    print(bottle.aloe_vera(5, 5))
    print(bottle.ficus(33, 11))
    
    print(calc.aloe_vera(10, 10))
    print(calc.ficus(44, 11))
    
    print(aloe_vera(20, 5))
    print(ficus(55, 11))
    
    print(div(66, 11))
    
main()