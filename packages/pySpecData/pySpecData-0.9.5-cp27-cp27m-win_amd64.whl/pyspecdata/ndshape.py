from pylab import *

class ndshape_base ():
    r'''The base ndshape class, which doesn't include an allocation method.'''
    def __init__(self,*args):
        self.zero_dimensional = False
        if len(args) == 2:
            self.shape = list(args[0])
            self.dimlabels = args[1]
        if len(args) == 1: #assum that it's an nddata object
            if hasattr(args[0],'dimlabels') and hasattr(args[0],'data'):# test that it's nddata without using any of the functions in core.py
                self.shape = list(args[0].data.shape)
                self.dimlabels = list(args[0].dimlabels)
                if len(self.shape) == 0 and len(self.dimlabels) == 0:
                    self.zero_dimensional = True
                    return
            else:
                raise ValueError('If you pass a single argument, it must be an nddata')
        return
    def __setitem__(self,reference,setto):
        self.shape[self.axn(reference)] = setto
        return
    def axn(self,axis):
        r'return the number for the axis with the name "axis"'
        try:
            return self.dimlabels.index(axis)
        except:
            raise ValueError(' '.join(map(repr,['there is no axis named',axis,'all axes are named',self.dimlabels])))
    def copy(self):
        try:
            return deepcopy(self)
        except:
            raise RuntimeError('Some type of error trying to run deepcopy on'+repr(self))
    def matchdims(self,arg):
        r'returns shape with [not in self, len 1] + [overlapping dims between arg + self] + [not in arg] --> this is better accomplished by using sets as I do in the matchdims below'
        for k in set(self.dimlabels) & set(arg.dimlabels):
            a = arg.shape[arg.axn(k)]
            b = self.shape[self.axn(k)]
            if a != b:
                raise CustomError('the',k,'dimension is not the same for self',self,'and arg',arg)
        if hasattr(arg,'dimlabels') and hasattr(arg,'data'):# test that it's nddata without using any of the functions in core.py
            arg = ndshape(arg)
        #{{{ add extra 1-len dims
        addeddims = set(self.dimlabels) ^ set(arg.dimlabels) & set(arg.dimlabels)
        self.dimlabels = list(addeddims) + self.dimlabels
        self.shape = [1] * len(addeddims) + list(self.shape)
        #}}}
        return self
    def __add__(self,arg):
        'take list of shape,dimlabels'
        shape = arg[0]
        dimlabels = arg[1]
        if type(shape) is str:
            shape,dimlabels = dimlabels,shape
        if isscalar(self.shape):
            self.shape = [self.shape]
        if isscalar(self.dimlabels):
            self.dimlabels = [self.dimlabels]
        if isscalar(shape):
            shape = [shape]
        if isscalar(dimlabels):
            dimlabels = [dimlabels]
        self.shape = shape + self.shape
        self.dimlabels = dimlabels + self.dimlabels
        return self
    def add_correctly(self,arg):
        '''take list of shape,dimlabels
        this is the correct function, until I can fix my back-references for add, which does it backwards'''
        shape = arg[0]
        dimlabels = arg[1]
        if type(shape) is str:
            shape,dimlabels = dimlabels,shape
        if isscalar(self.shape):
            self.shape = [self.shape]
        if isscalar(self.dimlabels):
            self.dimlabels = [self.dimlabels]
        if isscalar(shape):
            shape = [shape]
        if isscalar(dimlabels):
            dimlabels = [dimlabels]
        self.shape = self.shape + shape
        self.dimlabels = self.dimlabels + dimlabels
        return self
    def __repr__(self): #how it responds to print
        return zip(self.shape,self.dimlabels).__repr__()
    def __getitem__(self,args):
        try:
            mydict = dict(zip(self.dimlabels,self.shape))
        except:
            raise CustomError("either dimlabels=",self.dimlabels,"or shape",self.shape,"not in the correct format")
        try:
            return mydict[args]
        except:
            raise CustomError("one or more of the dimensions named",args,"do not exist in",self.dimlabels)
    def pop(self,label):
        r'remove a dimension'
        thisindex = self.axn(label)
        self.dimlabels.pop(thisindex)
        self.shape.pop(thisindex)
        return self
