
class ExprElement():

    varName = None

    def __init__(self, var):
        # print(type(str))
        if var is not None and var != '':
            self.varName = var
        else:
            self.varName = None





    '''
        返回表达式类型
    '''



    '''
        输出字符串
    '''
    def __repr__(self):
        if self.varName is None:
            return ''
        return str(self.varName)