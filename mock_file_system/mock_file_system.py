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
        # print(self, '<<<', newdir)
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
            nextdir = self.children[firstname]

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
    
    def __repr__(self) :
        return 'Directory: ' + self.name

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
    _currentdir = _currentdir.cd(destination)
    # print('Execute directory = ', _currentdir)
    tempvalue = command(*args)
    _currentdir = tempdir
    return tempvalue

if __name__ == '__main__' :
    _pwd()
    _mkdir('sub1')
    _mkdir('sub2')
    _mkdir('sub3')
    assert set(_ls()) == set(['sub1', 'sub2', 'sub3'])
    _exec('sub1', _mkdir, 'sub11')
    _exec('sub1', _mkdir, 'sub12')
    _exec('sub1', _mkdir, 'sub13')
    assert set(_exec('sub1', _ls)) == set(['sub11', 'sub12', 'sub13'])
    _cd('sub1')
    assert _pwd() == '/root/sub1/'

    # reset the Directory.
    # Trust the garbage collection lol.
    _currentdir = Directory('root')
    


        
    