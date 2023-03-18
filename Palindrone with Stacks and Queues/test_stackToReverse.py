from Queue import Queue
from Stack import Stack
from Palindrone_Assignment import stackToReverseString, reverseStringAndRemoveNonAlpha, isPalindrome, explorePalindrome

def test_stackToReverse1():
    calcStack = Stack()
    calcStack.push("A")
    calcStack.push("B")
    calcStack.push("B")
    calcStack.push("A")
    testResults = stackToReverseString(calcStack)
    assert testResults == "ABBA"
def test_isPalindrome1():
    phrase = "ABBA"
    result = isPalindrome(phrase)
    assert result == True
def test_isPalindrome2():
    phrase = "ABCBDA"
    result = isPalindrome(phrase)
    assert result == False
def test_isPalindrome3():
    phrase = "112"
    result = isPalindrome(phrase)
    assert result == False
def test_isPalindrome4():
    phrase = "A man, a plan, a canal: Panama"
    result = isPalindrome(phrase)
    assert result == True
def test_explorePalindrome5():
    phrase = "mug god: dog gum "
    results = explorePalindrome(phrase)
    assert results == True