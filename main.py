source = open('leaves.txt')

leaves = source.read()

import re
import random

line1_list = re.split(r'\n{1,}', leaves)

line1s_item = random.choice(line1_list)

print line1s_item
