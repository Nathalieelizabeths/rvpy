def numbers(*numberss):
    product=1
    
    for x in numberss:
        product*=x
    return product
#Write a function that takes a list of strings as input and 
#returns a new list that contains only the strings with more than 5 characters.
def filter_strings(*strings):
    result=[]
    for string in strings:
        if len(string)>5:
            result.append(string)
    return result

#Write a function that takes a string as input and returns true 
#if the string is a palindrome, false otherwise.
def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
#Write a function that takes a list of numbers as input and returns a 
#new list that contains the square of each number in the input list.
def square(numbers):
    squares=0
    for num in numbers:
        squares*2=num
    return squares
# 