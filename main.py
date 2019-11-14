source = open('leaves.txt')

leaves = source.read()

source2 = open('edcomplete.txt')

edcomplete = source2.read()

import re
import random

line1_list = re.findall(r'.+(?:\n)', leaves)
line2_list = re.findall(r'.+(?:\n)', edcomplete)

line1s_item = random.choice(line1_list)
line2s_item = random.choice(line2_list)
line3s_item = random.choice(line1_list)
line4s_item = random.choice(line2_list)


poem =  (line1s_item + "\r\n" + line2s_item + "\r\n" + line3s_item + "\r\n" + line4s_item)

print poem
