# 
#  x='',"",'""'
#x="hello
# x+="H1"
# print(l)
#x="hello"
#----------x-----------x--------x--------x-----
# Q1. Write a Python program to reverse the order of words in a given 
# string without reversing the individual words. 
# Input: "Hello World from Python" 
# Output: "Python from World Hello"
# x="hello everyone lets learn python"
# x=x.split()
# print(x)
# x.reverse()
# print(x)
# x=" ".join(x).capitalize()
# print(x)
#"python learn lets everyone hello"

# x="hello everyone lets learn python"
# # olleh enoyreve stel nrael nohtyp 
# x=x.split()
# #x.reverse()
# x=[word[::-1] for word in x]
# x=" ".join(x)
# print(x)

#----------x-----------x--------x--------x-----
# Q2. Write a Python program to remove all occurrences of a given 
# substring from a string. 
# Input: "This is a test string for testing", "test" 
# Output: "This is a string for ing" 

# x="This is a test string for testing"
# y="test"
# x=x.replace(y, "")
# print(x)


# Q3. Write a Python program that takes a string and a character as 
# input and returns a list of indices where the character occurs in the 
# string. 
# Input: "programming", 'm' 
# Output: [6, 7] 
# x="programming"
# y='m'
# result = [i for i, char in enumerate(x) if char == y]
# print(result)

#----------x-----------x--------x--------x-----

# Q4. Write a Python program to find all unique characters in a given 
# string. 
# Input: "programming" 
# # Output: ['p', 'o', ')r', 'g', 'a', 'm', 'i', 'n']
# x="programming"
# unique_chars = list(set(x))
# print(unique_chars)

#----------x-----------x--------x--------x-----

# Q5 Write a Python program to count the number of words in a given 
# string that start with a specific letter which was taken as a input. 
# Input: "This is a test string for testing", 't' 
# Output: 3
# x="This is a test string for testing"
# letter='t'
# words = x.split()
# count = sum(1 for word in words if word.startswith(letter))
# print(count)

#----------x-----------x--------x--------x-----

#//SET-P
# only store MUTABLE elements(NOT BE UPDATED)
#ONLY UNIQUE ELEMENTS STORE
#CAN'T ACCESS THE ELEMENTS WITH INDEX
#st=set()
#set store =tuples, string, int, float, bool
#set=set not store list
#

# lst=[6,4,5,4,3,5,2,244,4]
# lst=list(set(lst))
# print(lst)

# to add a single element into set we use add()
# s={1,2,3,4,5}
# s.add(6)
# print(s)
# s.update([5,2,6,7,5])
# print(s)
# s.remove(7)  
# # //remove karta hea 
# print(s)
# s.discard(5)  
# # //lement nahi ho to vaisa hi chhod deta hea
# print(s)
# # s.pop(5)
# s.clear()  #poora clear karta hea
# print(s)

# a={1,2,3,4}
# b={3,4,5,6}
# c={}

