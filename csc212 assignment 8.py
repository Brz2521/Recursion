# Assignment 8
# 1. reversed string

#Function that returns string to reverse the input of string
def reverse(input_string):
    if len(input_string) == 0:
        return
    p = input_string[0]
    reverse(input_string[1:])
    print(p)

input_string = "csc 212"

reverse(input_string)


#2. Recursive function

#from __future__ import print_function
def rec_string(str):
    if rec_string.count == 0:
        print("*")
    else:
        i = len(str) - rec_string.count
        while i < len(str):
            print(str[i], end='')
            i = i + 1
        print()
    if rec_string.count == len(str):
        return
    rec_string.count = rec_string.count + 1;
    rec_string(str);
rec_string.count = 0

rec_string('abcde')

# 3. Function for Euclid's algorithm
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,(a%b))
