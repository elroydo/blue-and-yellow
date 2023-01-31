def main():
    setSets()
    setComprehension()
    setUnion()
    setIntersection()
    setDifference()
    setSymmDifference()
    setIsSuperSubset()
    setDisjoint()
    
def setSets():
    #only unique items in sets
    empty = set()
    
    print(type(empty))
    
    if not empty:
        print(f"{empty} is empty")
        
    bevs = set(['tea', 'coffee', 'milk', 'tea'])
    
    print(f"{len(bevs)} items of {bevs}")
    
    bev = 'tea'
    if bev in bevs:
        print(f"Would you care for some milk with your {bev}?")
       
    bev = 'juice'
    if bev not in bevs:
        print(f"No {bev}")
        
    for index, bev in enumerate(bevs, 1):
        print(f"{index}. {bev}")
        
    bevs.add('juice')
    print(bevs)
    bevs.remove('milk')
    bevs.discard('rum')
    print(bevs)
    bevs.pop()
    print(bevs)
    bevs.clear()
    print(bevs)
    
    bevs = set(['tea', 'coffee', 'milk', 'tea'])
    bevs = frozenset(bevs) #immutable
    #bevs.add('juice') #exception; cannot add to frozen set
    
def setComprehension():
    anis = {'cats', 'dogs', 'Owls', 'Meerkats'}
    #{expression for element in set if condition}
    upper_anis = set(map(lambda a: a.upper(), anis))
    print(upper_anis)
    lower_anis = {ani.lower() for ani in anis}
    print(lower_anis)
    fe_anis = {ani.capitalize() for ani in anis if ani != 'cats'}
    print(fe_anis)
    
    
def setUnion():
    s1 = {'earth', 'wind', 'fire'}
    s2 = {'wind', 'water', 'aether'}
    
    s = s1.union(s2)
    print(s)
    s = s1 | s2
    print(s)
    
def setIntersection():
    s1 = {'a', 'b', 'c'}
    s2 = {'d', 'c', 'b'}
    
    s = s1.intersection(s2)
    #s = s1 & s2 #same thing as above
    print(s)
    
def setDifference():
    s1 = {'a', 'b', 'c'}
    s2 = {'d', 'c', 'b'}
    
    s = s1.difference(s2)
    #s = s1 - s2 #same thing as above
    print(s)
    
def setSymmDifference():
    s1 = {'a', 'b', 'c'}
    s2 = {'d', 'c', 'b'}
    
    s = s1.symmetric_difference(s2)
    #s = s1 ^ s2 #same thing as above
    print(s)
    
def setIsSuperSubset():
    a = {'a', 'b', 'c', 'd', 'e'}
    b = {'d', 'c', 'b'}
    
    x = b.issubset(a)
    #s = b <= a #same thing as above (< proper)
    print(x)
    
    x = b.issuperset(a)
    #s = b >= a #same thing as above (> proper)
    print(x)
    
def setDisjoint():
    a = {'z', 'y', 'x'}
    b = {'a', 'b', 'c'}
    
    print(a.isdisjoint(b))
    
main()