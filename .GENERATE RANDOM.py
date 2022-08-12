import random 
from random import seed
from random import randint
import string
import pyperclip
from easygui import choicebox
from easygui import enterbox
from easygui import multenterbox

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
    seed(1)
    n1, n2, n3 = n
    output = []
    for i in range(n1):
        value = randint(n2, n3)
        output.append(value)
    #print(output)
    output = ' '.join(map(str,output))
    pyperclip.copy(output)

def select():
    text = "Choose your preferred function:"
    title = "Function Selection"
    choices = ["Lowercase Only", "Uppercase Only", "All Letters", "Digits Only", "Punctuation Only","Array of Numbers"]
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
    else:
        quit()
  
def char_num_select():
    text = "Specify the number of characters to generate."
    title = "Character Number Entry"
    num = enterbox(text, title)
    if num == None:
        quit()
    num = int(num)
    return num

def array_num_select():
    text = "Select how many numbers to be generated and between what range they may fall."
    title = "Array Number Entry"
    input_list = ["Size of Array", "Lower Bound", "Upper Bound"]
    default_list = ["1", "1", "10"]
    output = multenterbox(text, title, input_list, default_list)
    if output == None:
        quit()
    output = list(map(int, output))
    n1, *n = output
    n2 = min(n)
    n3 = max(n)
    output = [n1,n2,n3]
    return output
 
if __name__ == "__main__":
    select()
