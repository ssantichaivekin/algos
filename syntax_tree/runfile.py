def runfile(filename,*args) :
    '''
    Run the file and return the output of the file.
    Takes args as the argument of the function in the file.
    Return the output as specified in a file.
    '''
    # all the files will have the line
    # output = function(*args)
    # at the end
    variables = { 'args': args }
    exec(open(filename).read(), variables)
    output = variables['output']
    return output