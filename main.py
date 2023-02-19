# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    result = 0
    opening_brackets_stack = []
    
    
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            left = Bracket(next, i)
            opening_brackets_stack.append(left)
            
            pass
        if next in ")]}":
            # Process closing bracket, write your code here
            pass
        
            if len(opening_brackets_stack) != 0:
                lastElement = opening_brackets_stack[len(opening_brackets_stack) - 1]
                if are_matching(lastElement.char, next) : 
                    opening_brackets_stack.remove(lastElement)
                else :
                    result = i + 1
                    return result
                return 'Success'
    if result == 0: 
        return 1  

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here

    print(mismatch)

if __name__ == "__main__":
    
    main()
