def main():
    a_list = ['a', 'list']
    gold = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    omni = [[3, 3], [66, 66]]
    
    print(a_list, gold, omni, omni[-1])
    
    a_list[0] = 'b'
    
    print(a_list[0])
    
    a_list.append('of')
    
    print(a_list)
    
    a_list.insert(2, 'lists')
    
    print(a_list)
    
    del omni[1]
    
    print(omni)
    
    print(gold.pop())
    print(gold)
    print(gold.pop(3))
    print(gold)
    gold.remove(21)
    print(gold)
    
main()