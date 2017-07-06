import time
import random
alphabet=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ""]
first_name=raw_input("What's your First Name?\n")
last_name=raw_input("What's your Last Name?\n")
print "Your name is " + first_name + " " + last_name + "."
full_name_computer = first_name + last_name
full_name_showing = first_name + " " + last_name
full_name_computer = str(full_name_computer)
length=len(full_name_computer)
full_name_computer.lower()
print "You have" , length , "letters in your name."
time.sleep(3)
print "Let's make a secret code!"
print "Let's see if you can figure it out!"
time.sleep(3)
letter_number=0
for x in range(length-1):
    first_letter=(full_name_computer[letter_number])
    first_letter=first_letter.upper()
    number_in_alphabet=alphabet.index(first_letter)
    encryption=(25-number_in_alphabet)
    print (alphabet[encryption])
    letter_number=letter_number + 1
