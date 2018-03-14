class Directory :
    def __init__(self, name, comment=None, parent=None) :
        '''
        Initialize a directory with no subdirectory.
        '''
        self.name = name
        self.parent = parent
        self.comment = comment
        self.children = {}
    
    def mkdir(self, dirname, dircomment=None) :
        '''
        Make a subdirectory in self.
        '''
        newdir = Directory(dirname, comment=dircomment, parent = self)
        self.children[dirname] = newdir
    
    def pwd(self) :
        '''
        Return the name of the current directory.
        '''
        if self.parent == None :
            return '/' + self.name + '/'
        else :
            return  self.parent.pwd() + self.name + '/'

    def cd_helper(self, targetarr) :
        '''
        A recursive helper for cd.
        '''
        firstname = targetarr[0]
        targetarr = targetarr[1:]
        if firstname == '.' : 
            nextdir = self
        elif firstname == 'root' :
            nextdir = currentdir.gotoroot()
        elif firstname == '..' :
            nextdir = self.parent
        else :
            nextdir = self.children[targetarr[0]]

        if targetarr :
            return nextdir.cd_helper(targetarr)
        else :
            return nextdir

    def cd(self, targetname) :
        '''
        Return the requested directory targetname that is a subfolder
        of the object being called.
        '''
        targetarr = targetname.split('/')
        return self.cd_helper(targetarr[1:])
        
        return self.cd_helper(targetarr)
    
    def setcomment(self, newcomment) :
        '''
        Set the comment of the directory.
        '''
        self.comment = newcomment
    
    def ls(self) :
        '''
        Print all subfolder (children) of the directory.
        '''
        return [ key for key in self.children ]
    
    def getcomment(self) :
        '''
        Get the comment of the directory.
        '''
        return self.comment
    
    def parent(self) :
        '''
        Return the parent of self.
        '''
        return self.parent
    
    def gotoroot(self) :
        '''
        Go back to the root recursively.
        '''
        if not self.parent :
            return self
        else :
            return gotoroot(self.parent)

_currentdir = Directory('root')

def _pwd() :
    '''
    Return the directory of the current directory.
    '''
    global _currentdir
    return _currentdir.pwd()

def _cd(targetname) :
    '''
    Go to the directory specified.
    '''
    global _currentdir
    _currentdir = _currentdir.cd(targetname)

def _mkdir(targetname) :
    '''
    Make the directory in the current directory.
    '''
    global _currentdir
    _currentdir.mkdir(targetname)

def _ls() :
    '''
    List items in the current directory.
    '''
    global _currentdir
    return _currentdir.ls()

def _setcomment(comment) :
    '''
    Set the comment of the current directory.
    '''
    global _currentdir
    _currentdir.setcomment(comment)

def _exec(destination, command, *args) :
    '''
    Go to the destination folder to execute the command.
    And then come back to the current directory.
    '''
    global _currentdir
    tempdir = _currentdir
    _currentdir.cd(destination)
    command(*args)
    _currentdir = tempdir


        
    