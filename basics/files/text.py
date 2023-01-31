import os.path #same as bottom
from os.path import exists ##existence~
from pathlib import Path #pathing

def main():
    #r (read), w (write), a (append)
    with open('faux.txt', 'r') as e:
        lines = e.read() #line and lines
        #e.close() #no need with 'with'
        print(lines)
        #[print(line) for line in e.readlines()]
        
    writing()
    creating()
    existing()
        
        
def writing():
    lines = ['The quick brown', 'fox jumped over', 'the lazy dog.']
    dots = ['Then the dog', 'melted into the', 'ground.']
    with open('test.txt', 'w') as f:
        f.write('physiognomy')
        for line in lines:
            f.write(line)
            f.write('\n')
            
    with open('test.txt', 'w') as f:
        f.write('\n'.join(lines))
        
    with open('test.txt', 'a', encoding='utf-8') as f:
        f.write('\n'.join(dots))
        
def creating():
    quark = 'Three quarks for Muster Mark!'
    try: 
        with open('quark.txt', 'w') as f: #x for no new
            f.write(quark)
    except FileNotFoundError:
        print("the directory doesn't exist")
        
def existing():
    print(os.path.exists('faux.txt'))
    print(exists('faux.txt'))
    print(Path('fake.txt').is_file())
    
print(__name__)
main()