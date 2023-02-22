import StackedLinkedList as sl
import Queue as q

nonAlpha = ["!", "?", ".", ",", ":", ";", ")", "(", "&", "*", "+", "-", "|", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " "]
def stackToReverseString(phrase):
    #create empty stack and queue
    stack = sl.Stack()

    #iterate through palindrome
    for letter in phrase:
        #add letter to stack
        stack.push(letter)


def reverseStringAndNonAlpha(phrase):
    #create empty queue and stack
    stack = sl.Stack()

    #iterate through palindrome
    for char in phrase:
        if char in nonAlpha:
            stack.push(char)
        else:
            #add letter to queue
            queue.enqueue(char)
    #push each letter to queue and check if it is a palindrome

    #push each letter to stack and check if it is a palindrome

    #compare stack and queue and return true or false if palindrome


def isPalindrome(stack, queue):
    #compare stack and queue and return true or false if palindrome