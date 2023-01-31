def main():
    empty = {}
    
    print(type(empty))
    
    person = {
        'name': 'John Doe',
        'age': 33,
        'sex': 'male',
        'alive': True
    }
    
    print(person['age'])
    print(person.get('job', 'Parameter doesn\'t exist.'))
    
    person['job'] = 'Plane'
    person['age'] = '44'
    print(person)
    
    del person['alive']
    print(person.items())
    #keys and values
    for key, value, in person.items():
        print(f"{key}: {value}")
    #keys
    for key in person.keys():
        print(key)
    #values
    for value in person.values():
        print(value)
        
    #comprehensions with dictionaries
    fruits = {
        'Apples': 2,
        'Bananas': 1,
        'Oranges': 2,
        'Strawberries': 3
    }
    #increasing prices
    up_fruits = {fruit: price * 1.03 for (fruit, price) in fruits.items()}
    print(up_fruits.items())
    
    #filtering fruits
    sel_fruits = {f: p for (f, p) in fruits.items() if p > 1}
    print(sel_fruits)
    
main()