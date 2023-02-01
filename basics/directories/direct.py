import os
import time

def main():
    #current working directory
    print(os.getcwd())
    os.chdir('test')
    print(os.getcwd())
    
    #for different platforms
    p = os.path.join('data', 'temp')
    print(p)
    s = os.path.split(p)
    print(s)
    
    dir = os.path.join('C:\\', 'DRIVERS')
    print(dir)
    #traverse dir
    for root, dirs, files in os.walk(dir):
        print("{0} has {1} files".format(root, len(files)))
    
    #check existence
    if os.path.exists(dir) or os.path.isdir(dir):
        print(f'{dir} is directory')
        
    removeApprry()
        
    #create
    if not os.path.exists('apple'):
        os.mkdir('apple')
    
    time.sleep(1)
    #rename
    if os.path.exists('apple') or os.path.isdir('apple'):
        os.rename('apple', 'cherry')
        print("'{0}' renamed to '{1}'".format('apple', 'cherry'))
        
    time.sleep(1)
    removeApprry()
    
def removeApprry(): #delete dir
    if os.path.exists('cherry'):
        os.rmdir('cherry')
        print('success delete')
    elif os.path.exists('apple'):
        os.rmdir('cherry')
        print('success delete')
    else:
        print('no existence')
        
main()