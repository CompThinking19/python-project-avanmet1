#Poem 1 Is laid out in quatrains as this was a form that the poetry of both Poe and Dickinson often took, even outside of their famous ballads.  The lines of this poem are aranged to alternate very other line between the words of Dickinson and then Poe.
source1 = open('edcomplete.txt')
source2 = open('poecomplete.txt')
#used open function to open the txt files I will be using as the source of random lines for the project

ed = source1.read()
poe = source2.read()

import re
import random
#imported regex for to search txt files for individual lines of poetry (everything except repeated line breaks)
#imported random module for randomly selecting lines of poetry

list1 = re.findall(r'.+(?:\n)', ed)
list2 = re.findall(r'.+(?:\n)', poe)
#these 2 lists are created using finall function and a regex expression that selects all consecutive text and puts it into a list, creating a new item every line break.  this ensures that each item in each list will be a single line of poetry
#this regex expression ignores more than one line break, ensuring that spaces between poems and stanzas are not included as items in each list

line1_item = random.choice(list1) #the body of the poems being generated is accomplished through a series of variables created using the random choice function to put a random line of poetry from the desired list into each variable
list1.remove(line1_item) #used remove to make sure that the value contained in the previous variable will not be repeated again, ensuring that the final result will not be overly repetative regardless of the list size
line2_item = random.choice(list2) #the code repeats in this way, divided into 4 stanzas of poetry with each line being represented by a variable in the code
list2.remove(line2_item)
line3_item = random.choice(list1)
list1.remove(line3_item)
line4_item = random.choice(list2)
list2.remove(line4_item)

line5_item = random.choice(list1)
list1.remove(line5_item)
line6_item = random.choice(list2)
list2.remove(line6_item)
line7_item = random.choice(list1)
list1.remove(line7_item)
line8_item = random.choice(list2)
list2.remove(line8_item)

line9_item = random.choice(list1)
list1.remove(line9_item)
line10_item = random.choice(list2)
list2.remove(line10_item)
line11_item = random.choice(list1)
list1.remove(line11_item)
line12_item = random.choice(list2)
list2.remove(line12_item)

line13_item = random.choice(list1)
list1.remove(line13_item)
line14_item = random.choice(list2)
list2.remove(line14_item)
line15_item = random.choice(list1)
list1.remove(line15_item)
line16_item = random.choice(list2)
list2.remove(line16_item)


stanza1 = (line1_item + line2_item + line3_item + line4_item)
stanza2 = (line5_item + line6_item + line7_item + line8_item)
stanza3 = (line9_item + line10_item + line11_item + line12_item)
stanza4 = (line13_item + line14_item + line15_item + line16_item)

import os #trying to print line breaks between stanzas kept throwing errors
#I could not figure out how to resolve them; looked up solutions on stack overflow and decided to use os.linesep to sidestep issue with regular python syntax

poem1 = (stanza1 + os.linesep + stanza2 + os.linesep + stanza3 +os.linesep + stanza4)

print "Poem 1" + os.linesep + poem1


#Poem 2 is also laid out in quatrains but differs in that the first 2 lines of each stanza sample Poe and the last lines of each stanza sample Dikinson. The code is exactly the same, I have just changed which list a random item is being pulled from for each variable.

line1s_item = random.choice(list2)
list2.remove(line1s_item)
line2s_item = random.choice(list2)
list2.remove(line2s_item)
line3s_item = random.choice(list1)
list1.remove(line3s_item)
line4s_item = random.choice(list1)
list1.remove(line4s_item)

line5s_item = random.choice(list2)
list2.remove(line5s_item)
line6s_item = random.choice(list2)
list2.remove(line6s_item)
line7s_item = random.choice(list1)
list1.remove(line7s_item)
line8s_item = random.choice(list1)
list1.remove(line8s_item)

line9s_item = random.choice(list2)
list2.remove(line9s_item)
line10s_item = random.choice(list2)
list2.remove(line10s_item)
line11s_item = random.choice(list1)
list1.remove(line11s_item)
line12s_item = random.choice(list1)
list1.remove(line12s_item)

line13s_item = random.choice(list2)
list2.remove(line13s_item)
line14s_item = random.choice(list2)
list2.remove(line14s_item)
line15s_item = random.choice(list1)
list1.remove(line15s_item)
line16s_item = random.choice(list1)
list1.remove(line16s_item)


stanza1s = (line1s_item + line2s_item + line3s_item + line4s_item)
stanza2s = (line5s_item + line6s_item + line7s_item + line8s_item)
stanza3s = (line9s_item + line10s_item + line11s_item + line12s_item)
stanza4s = (line13s_item + line14s_item + line15s_item + line16s_item)

poem2 = (stanza1s + os.linesep + stanza2s + os.linesep + stanza3s +os.linesep + stanza4s)

print "Poem 2" + os.linesep + poem2
