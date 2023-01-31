import sys

def main():
    for path in sys.path:
        print(path)
        
main()

'''
#python module search path modification ref
import sys
sys.path.append('d:\\modules\\')
'''