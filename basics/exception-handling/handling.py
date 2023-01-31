def main():
    num = 0
    
    print("Please enter a positive number")
    while True:
        try:
            num = int(input('> '))
            break
        #except:
            print('Please enter a number')
        except ValueError:
            print('Invalid input')
            #can do individual errors
        except Exception as error:
            print(error)
        #else:
            #print(num)
        finally:
            print('There\s no escape!')
                
    print(f"a {num}?")
    
main()