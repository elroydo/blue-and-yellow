def main():
    abc = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
    abc.sort()
    print(abc)
    
    abc.sort(reverse=True)
    print(abc)
    
    #also works with numbers
    
    users = [
        ('John', 'Doe', 44),
        ('Jane', 'Doe', 33),
        ('Joe', 'Doe', 22)
    ]
    
    #ascending by first name
    users.sort()
    print(users)
    
    #descending age using function
    users.sort(key=sort_key, reverse=True)
    print(users)
    
    #ascending age using lambda function
    users.sort(key=lambda user: user[2])
    print(users)
    
    
def sort_key(user):
    return user[2]
    
main()