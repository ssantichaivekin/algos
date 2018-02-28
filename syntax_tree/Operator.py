'''
Class operator define operator,
how many arguments it gets, how to read (read 
via left to right or right to left), (or is it
a prefix, suffix?) and how to evaluate such operators.
'''
import re

class Operator:
    
    def __init__(self, name, symbol, prec, num, rule) :
        '''
        Initialize the Operator.
        '''
        self.name = name
        self.symbol = symbol
        # Note that the prec is defined as the precedence
        # of the operator. It is either 'prefix' 'suffix'
        # or 'infix'.
        self.prec = prec
        # This is the number of arguments. This is for
        # prefix and suffix.
        # Prefix and Suffix can have any number of arguments.
        # We have to specify it.
        self.num = num
        # The rule specifies how to use the operator.
        # The rule follows this format:
        # The first position is being addressed as a,
        # second as b, third as c, and so on.
        # For example, increment can be written as 'a+1'
        # Add can be written as 'a+b'
    
    def get_regex(self) :
        '''
        Return the regex matcher obj of the operator.
        '''
        
        
    