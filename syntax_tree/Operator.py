'''
Class operator define operator,
how many arguments it gets, how to read (read 
via left to right or right to left), (or is it
a prefix, suffix?) and how to evaluate such operators.
'''
import re
from runfile import runfile

class Operator:

    def read_regex_from_file(filename) :
        '''
        Return the regex pattern from filename.
        '''
        return open(filename).read().strip('\'')

    def __init__(self, name, symbol, regexfilename, runfilename) :
        '''
        Initialize the Operator.
        '''
        self.name = name
        # symbol as is represented in the tree.
        self.symbol = symbol
        # regex filename is used to read for the regex file.
        self.regex_pattern = read_regex_from_file(regexfilename)
        self.runfilename = runfilename
    
    def run(self, *args) :
        '''
        Run the operator on the input argument.
        For example, we would write :
          > add_op.run(1, 2, 3, 4, 5)
          15
        '''
        return runfile(self.runfilename, *args)
        
        
    