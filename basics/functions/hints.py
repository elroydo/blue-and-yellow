from typing import Union

def main():
    print(hint(333))
    
    val: str = 'Bob'
    print(hint(val))
    
    a: Union[int, float] = 3
    print(add(a, 4))
    
    l: list = [1, 2, 3]
    l = {1: 'one', 2: 'two', 3: 'three'}
    print(l)
    
    void('bagels')
    
def hint(msg: str) -> str:
    return f'hola {msg}'

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y

def void(msg: str) -> None:
    print(msg)

main()