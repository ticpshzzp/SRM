
class ExprElement():

    varName = None

    def __init__(self, str):
        # print(type(str))
        if str is not None and str != '':
            self.varName = str
        else:
            self.varName = None

    pass

    '''
        返回表达式类型
    '''



    '''
        输出字符串
    '''
    def __repr__(self):
        if self.varName is None:
            return ''
        return self.varName