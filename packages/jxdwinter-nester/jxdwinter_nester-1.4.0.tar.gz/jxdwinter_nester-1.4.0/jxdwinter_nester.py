
# coding:UTF-8

import sys
import os

'''This is the "nester.py" module and it provides one function called print_lol()
which prints lists that may or may not include nested list.'''

def print_lol(the_list, indent = False ,level = 0, fh = sys.stdout) :
    '''This functin eakes one positional argument called "the list", which
    is any Python list (of - possibly - nested lists). Each data item in the provided list is 
    (recursively) printed to the screen on it'.s own line. '''
    for each_item in the_list :
        if isinstance(each_item,list) :
            print_lol(each_item, indent ,level + 1,fh)
        else :
            if indent :
                for tab_stop in range(level):
                    print("\t",end='',file = fh)
            print(each_item,file = fh)