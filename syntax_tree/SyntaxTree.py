'''
A class of SyntaxTree.
Given an series of operations like '3 + 5 * 2 + (5*5)'
Return a tree-like structure of operations and
its operands.
Also support eveluate syntax tree.
'''

class SyntaxTree:

    def __init__(self, operator, operands) :
        '''
        Initialize the SyntaxTree
        '''
        self.operator = operator
        # operand is a list of SyntaxTree or Value
        self.operands = operands

    def evaluate(self) :
        '''
        Evaluate the SyntaxTree recusrively.
        '''
        opera


    