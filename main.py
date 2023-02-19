# python3

from collections import namedtuple
import fileinput

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
            pass

        if next in ")]}":
            if(len(opening_brackets_stack) == 0 or not are_matching(opening_brackets_stack[len(opening_brackets_stack)-1].char, next)):
                print(i+1)
                break
            opening_brackets_stack.pop()
            pass
    
    return opening_brackets_stack

def main():
    ievade = input()
    text =  ""
    if ievade == "F":
        text = fileinput.input()
    if ievade == "I":
        text = input()
    mismatch = find_mismatch(text)
    if (len(mismatch) == 0):
        print("Success")
    else:
        print(mismatch[len(mismatch)-1].position)
    


if __name__ == "__main__":
    main()
