def main(): #manipulating lists
    groc = ['bread', 'butter', 'eggs', 'milk']
    sub_groc = groc[2:4]
    nfirst_groc = groc[:2]
    nlast_groc = groc[-2:]
    nth_groc = groc[::2] #every nth element
    rev_groc = groc[::-1] #reverse
    groc[0:2] = ['bricks', 'mortar']
    
    print(groc, sub_groc)
    print(nfirst_groc, nlast_groc, nth_groc)
    print(rev_groc)
    print(groc)
    print(f"list has {len(groc)} elements")
    groc.remove('milk')
    print(f"list has {len(groc)} elements")
    
main()