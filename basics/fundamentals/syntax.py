#defining main function
def syntax():
        i = 0
        max = 9
        while (i <= max):
            print(i)
            i = i + 1
#indentation and whitespaces
            
def backslash():
    a = 3
    b = 6
    c = 3  
    if (a != b) and (b != c) and \
        (c == a):
        print("The owls are not what they seem")
#contiue statements to multiple lines using a backslash

def identifiers():
    _counter = 0
    while (_counter < 3):
        print(_counter)
        _counter = _counter + 1
#underscores, cases, and keywords

import keyword
def keywords():
    print(keyword.kwlist)
#special meanings to dear python

def theory():
    s = 'string'
    print(s)
    s = "strings"
    print(s)
    s = '''strings
        strings
        strings'''
    print(s)
#strings and literals

#calling functions        
syntax()
backslash()
identifiers()
keywords()
theory()

#notes
""" interprets each line into machine code
clear, uniform, and elegant... """