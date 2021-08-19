from Expr.ExprElement import ExprElement


class TailExpr(ExprElement):
    mVar = None
    mTail = None

    def __init__(self, var: ExprElement, tail: ExprElement):
        self.mVar = ExprElement(var)
        # print("--", type(var), var)
        # print("--", type(self.mVar))
        self.mTail = tail
        print(self.mVar)
        print(self.mTail)


    '''
        输出格式化
    '''
    def __repr__(self):
        rst = str(self.mVar)
        if str(self.mTail) != '':
            rst += "--" + str(self.mTail)
        return rst


    pass
