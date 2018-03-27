'''
Class operator define operator,
how many arguments it gets, how to read (read 
via left to right or right to left), (or is it
a prefix, suffix?) and how to evaluate such operators.
'''
import re

class Operator:
    
    def __init__(self, name, symbol, regexfilename, runfilename) :
        '''
        Initialize the Operator.
        '''
        self.name = name
        # symbol to be represented in the tree.
        self.symbol = symbol
        # file
    
    def get_regex(self) :
        '''
        Return the regex matcher obj of the operator.
        '''
        
        
    