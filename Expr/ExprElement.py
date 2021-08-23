
class ExprElement():

    varName = None

<<<<<<< HEAD
    def __init__(self, str):
        # print(type(str))
        if str is not None and str != '':
            self.varName = str
        else:
            self.varName = None

    pass
=======
    def __init__(self, var):
        # print(type(str))
        if var is not None and var != '':
            self.varName = var
        else:
            self.varName = None




>>>>>>> 1019c1cd9a1955b7918d9526fcbec2bdc9039439

    '''
        返回表达式类型
    '''



    '''
        输出字符串
    '''
    def __repr__(self):
        if self.varName is None:
            return ''
<<<<<<< HEAD
        return self.varName
=======
        return str(self.varName)
>>>>>>> 1019c1cd9a1955b7918d9526fcbec2bdc9039439
