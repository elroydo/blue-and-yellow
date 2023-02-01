import csv
import os

def main():
    readingCSV()
    dictReadingCSV()
    writingCSV()
    god()
            
    
def readingCSV():
    f = open('test.csv', encoding='UTF8')
    #reader is useful, but has limitations
    csv_reader = csv.reader(f)
    
    for n in csv_reader:
        print(n)
        
    f.close()
    
    print('\n------------------------------\n')
    
    total_price = 0
    
    #no need to close() file with bellow
    with open('test.csv', encoding='UTF8') as f:
        r = csv.reader(f)
        #next(r) #skips a line, i.e., header
        for row, n in enumerate(r, 1): #enumerate specifies index
            if row == 1:
                print(f'header:\n{n}\ndata:')
            else:
                print(n)
                total_price += float(n[4])#5th column
    
    print(f'total price = {total_price}')
    
def dictReadingCSV():
     #fieldnames = ['val', 'thing', 'name', 'qty', 'price'] #example
    #dictreader comes to save the day
    with open('test.csv', encoding='utf8') as f:
        r = csv.DictReader(f) 
        #r = csv.DictReader(f, fieldnames) #fieldnames not necessary
        next(r) #skip header
        
        for n in r:
            print(f"{n['name']} from {n['thing']} bought {n['qty']} for £{n['price']}.")


def writingCSV():
    header = ['name', 'sex', 'age']
    data = [
        ['John Doe', 'm', 30],
        ['Jane Doe', 'f', 40],
        ['Bob Doe', 'm', 50]
    ]
    
    fieldnames = ['name', 'sex', 'age', 'animal'] 
    rows = [
        {'name': 'Jane Doe',
         'sex': 'f',
         'age': 3000,
         'animal': 'owl'},
        {'name': 'John Doe',
         'sex': 'm',
         'age': 10000,
         'animal': 'meerkat'},
        {'name': 'Jen Doe',
         'sex': 'f',
         'age': 3000000,
         'animal': 'pinniped'}
    ]
    
    #using reader
    with open('banana.csv', 'w', newline='') as f:
        w = csv.writer(f, )
        w.writerow(header)
        w.writerows(data)
        
    #using dictwriter
    with open('banana.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
        #cool
        
def god():
    existence = 'universe.txt'
    
    #creates new
    open(existence, 'x')
    
    #if os.path.exists(existence):
        #os.remove(existence)
        
    try:
        os.rename(existence, 'omniverse.txt')
        os.remove(existence)
        #just like that... in a flash!
    except FileNotFoundError as e:
        print(e)
    except FileExistsError as e:
        print(e)

print(__name__)
main()
