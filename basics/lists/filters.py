def main():
    values = [10, 100, 20, 200, 30, 300, 40, 400]
    
    filtered = filter(lambda val: val >= 50, values)
    print(list(filtered))
    
    people = [
        ['John Doe', 44],
        ['Jane Doe', 33],
        ['Joe Doe', 22],
        ['Jill Doe', 15]
    ]
    
    peopled = filter(lambda p: p[1] >= 18, people)
    print(list(peopled))
    
main()