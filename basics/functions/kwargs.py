def main():
    #can accept keyword args as dictionary
    connect(a='a', b=3, c='c')
    connect(server='localhost', port=3306, user='root', password='toor')
    
    config = {
        'server': 'localhost',
        'port': 3306,
        'user': 'admin',
        'password': 'admin'
    }
    connect(**config) #passing a dictionary into fn **
    ##kwarg comes after othe params to avoid errors
    
    fn()
    fn(1, 3, a=9, b=24)
    
def connect(**kwargs):
    print(type(kwargs))
    print(kwargs)
    
def fn(*args, **kwargs):
    print(args)
    print(kwargs)
    
main()