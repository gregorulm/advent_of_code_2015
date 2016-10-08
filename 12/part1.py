# AoC: Day 12

import json
from pprint import pprint


"""

https://docs.python.org/2.7/library/json.html

JSON 	        Python
object 	        dict
array 	        list
string 	        unicode
number (int) 	int, long
number (real) 	float
true 	        True
false 	        False
null 	        None

"""


total = 0

with open('input') as data_file:    
    data = json.load(data_file)

# recursively traverse dictionary
def findIntegers(inp):
    global total
    
    if isinstance(inp, dict):
        for key in inp.keys():
            findIntegers(inp[key])
        
    elif isinstance(inp, list):
        for elem in inp:
            findIntegers(elem)

    elif isinstance(inp, unicode):
        return
        
    elif isinstance(inp, int):
        total += inp
        
    else:
        print "xxx", type(inp)
    
    
findIntegers(data)

print total    
    


