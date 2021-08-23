from Expr.TailExpr import TailExpr


class PathExpr(TailExpr):

    # def __init__(self, var, tail):
    #     self.mVar = var
    #     self.mTailer = tail

    '''
            输出格式化
        '''

    def __repr__(self):
        rst = str(self.mVar)
        if str(self.mTail) != '':
            rst += "::" + str(self.mTail)
        return rst