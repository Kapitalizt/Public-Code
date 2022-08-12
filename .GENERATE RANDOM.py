import random
import string
import pyperclip
from easygui import *

# 1 LOWERCASE
def lower(n):
    l = string.ascii_lowercase
    output = ''.join(random.choice(l) for i in range(n))
    #print(output)
    pyperclip.copy(output)

# 2 UPPERCASE
def upper(n):
    l = string.ascii_uppercase
    output = ''.join(random.choice(l) for i in range(n))
    #print(output)
    pyperclip.copy(output)

# 3 LETTERS
def letters(n):
    l = string.ascii_letters
    output = ''.join(random.choice(l) for i in range(n)) 
    #print(output)
    pyperclip.copy(output)

# 4 DIGITS
def digits(n):
    l = string.digits
    output = ''.join(random.choice(l) for i in range(n)) 
    #print(output)
    pyperclip.copy(output)

# 5 PUNCTUATION
def punctuation(n):
    l = string.punctuation
    output = ''.join(random.choice(l) for i in range(n)) 
    #print(output)
    pyperclip.copy(output)

# 6 NUMBER ARRAY
def num_array(n):
    #Generate 1000 random numbers between 1 and 5000000
    output = random.sample(range(n[1], n[2]), n[0])
    #print(output)
    output = ' '.join(map(str,output))
    
    pyperclip.copy(output)

def select():
    # message to be displayed
    text = "Selected any one item"
    # window title
    title = "Window Title GfG"
    # item choices
    choices = ["Lowercase Only", "Uppercase Only", "All Letters", "Digits Only", "Punctuation Only","Array of Numbers"]
    # creating a button box
    choice = choicebox(text, title, choices)

    if choice == "Lowercase Only":
        lower(char_num_select())
    elif choice == "Uppercase Only":
        upper(char_num_select())
    elif choice == "All Letters":
        letters(char_num_select())
    elif choice == "Digits Only":
        digits(char_num_select())
    elif choice == "Punctuation Only":
        punctuation(char_num_select())
    elif choice == "Array of Numbers":
        num_array(array_num_select())
  
def char_num_select():
    # message to be displayed
    text = "Specify the number of characters to generate."
    # window title
    title = "Character Number Entry"
    # default text
    d_text = ""
    # creating a enter box
    num = int(enterbox(text, title, d_text))
    return num

def array_num_select():
    # message to be displayed
    text = "Select how many numbers to be generated and between what range they may fall."
    # window title
    title = "Array Number Entry"
    # list of multiple inputs
    input_list = ["Size of Array", "Lower Bound", "Upper Bound"]
    # list of default text
    default_list = ["1", "1", "10"]
    # creating a integer box
    output = multenterbox(text, title, input_list, default_list)
    output = list(map(int, output))
    n1, *n = output
    n2 = min(n)
    n3 = max(n)
    output = [n1,n2,n3]
    return output
 
#choice = int(input())
#num = int(input())
"""
# title for the message box
title = "Message Box"
# message
message = "You selected : " + str(choice) + \n\n" + 
# creating a message box 
msg = msgbox(message, title)
"""

if __name__ == "__main__":
    select()