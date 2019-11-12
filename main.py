source = open('leaves.txt')

leaves = source.read()

import re
import random

line1_list = re.split(r'\n{1,}', leaves)

line1s_item = random.choice(line1_list)
line2s_itme = random.choice(line1_list)

poem =  (line1s_item + "\r\n" + line2s_item)

print poem
