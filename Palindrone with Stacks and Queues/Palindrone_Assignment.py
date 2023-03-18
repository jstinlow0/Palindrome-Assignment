import Stack as s
import Queue as q

nonAlpha = ["!", "?", ".", ",", ":", ";", ")", "(", "&", 
            "*", "+", "-", "|", " ", "1", "2","3","4","5",
            "6","7", "8", "9", "0", "@", "#","$","%", "^", "_"
            "=", "[", "]", "<",">"]

'''take a stack and turn into a string''' 

def stackToReverseString(instack:s.Stack):
    #create empty string
    string = ""
    while not instack.is_empty():
        temp= instack.pop()
        string = string + temp
    return string


'''removes non alpha characters from string and pushes the new string onto the stack and queue'''
def reverseStringAndRemoveNonAlpha(phrase):
    #create empty stack
    stack = s.Stack()
    queue = q.Queue()
    #pushes character to stack
    for char in phrase:
        if char not in nonAlpha:
            stack.push(char)
            queue.enqueue(char)
    
    #revmove non alpha characters from phrase
    #rev_stack, queue = stackToReverseString(stack)
    return stack,queue
    

'''checks to see if a string is a palindrome'''
def isPalindrome(phrase: str):
    #queue = q.Queue()
    phrase = phrase.lower()

    #removes unwanted characters and pushes the string onto a stack
    stack, queue = reverseStringAndRemoveNonAlpha(phrase)

    #checks if stack is empty
    if stack.is_empty():
        return False
    
    while not stack.is_empty():
        if stack.pop()!= queue.dequeue():
            return False
        
    return True
