# python3

from collections import namedtuple
import os

Bracket = namedtuple("Bracket", ["char", "position"])

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()
  
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    #result = 0
    isBracketFound = False
    opening_brackets_stack = []
    
    for i, next in enumerate(text):
        if next in "([{":
            isBracketFound = True
            left = Bracket(next, i)
            opening_brackets_stack.append(left)
            
            pass
        if next in ")]}":
            isBracketFound = True
            if len(opening_brackets_stack) != 0:
                lastElement = opening_brackets_stack[len(opening_brackets_stack) - 1]
                if are_matching(lastElement.char, next) : 
                    opening_brackets_stack.remove(lastElement)
                else :
                    #result = i + 1
                    return i + 1
                return 'Success'
    if isBracketFound == False:
        return 'Success'
    else:
        return 1

def main():
    path = os.getcwd() + '/test'
    os.chdir(path)
    #check = input()
    #if check == 'F':
    for file in os.listdir():
        file_path = f"{path}/{file}"
        text = read_text_file(file_path)
        mismatch = find_mismatch(text)
        print(mismatch)
    #if check == "I":
    #    text = input()
    #    mismatch = find_mismatch(text)
    #    print(mismatch)

if __name__ == "__main__":
    main()
