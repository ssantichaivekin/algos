'''
Defines an operator.
An operator has its own rege pattern signature and
its own way to execute itself. These are defined in
seperate files in Operator definitions.
'''
import re
from runfile import runfile

class Operator:

    def read_regex_from_file(self, filename) :
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
        self.regex_pattern = self.read_regex_from_file(regexfilename)
        self.runfilename = runfilename
    
    def run(self, *args) :
        '''
        Run the operator on the input argument.
        For example, we would write :
          > add_op.run(1, 2, 3, 4, 5)
          15
        '''
        return runfile(self.runfilename, *args)

if __name__ == '__main__' :
    # Tests :
    add_run = 'operators_definitions/add_exec.py'
    add_pattern = 'operators_definitions/add_pattern.py'
    add_op = Operator('add', '+', add_pattern, add_run)
    assert add_op.regex_pattern == r'(.+)\+(.+)'
    assert add_op.run(1, 2) == 3
        
        
    