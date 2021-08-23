from Expr.TailExpr import TailExpr


class PathExpr(TailExpr):

    # def __init__(self, var, tail):
    #     self.mVar = var
    #     self.mTailer = tail

    '''
<<<<<<< HEAD
            输出格式化
        '''
=======
        输出格式化
    '''
>>>>>>> 1019c1cd9a1955b7918d9526fcbec2bdc9039439

    def __repr__(self):
        rst = str(self.mVar)
        if str(self.mTail) != '':
            rst += "::" + str(self.mTail)
        return rst