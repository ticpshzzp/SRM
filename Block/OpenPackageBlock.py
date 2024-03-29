from Antlrtest import testParser
from Block.BaseBlock import BaseBlock
from Expr.ExprElement import ExprElement
from Expr.PathExpr import PathExpr


class OpenPackageBlock(BaseBlock):
    path = None

    def __init__(self, ctx:testParser.testParser.PathContext):
        if len(ctx.children) & 1:
<<<<<<< HEAD
            self.build(ctx)
        else:
            print("OpenPackageBlock::error")

    def build(self, ctx:testParser.testParser.PathContext):
=======
            self.Build(ctx)
        else:
            print("OpenPackageBlock::error")

    def Build(self, ctx:testParser.testParser.PathContext):
>>>>>>> 1019c1cd9a1955b7918d9526fcbec2bdc9039439
        length = len(ctx.children)//2
        tail = PathExpr(str(ctx.children[(length)*2]), ExprElement(None))
        for i in range(length):
            tail = PathExpr(str(ctx.children[(length-i-1)*2]), tail)
        self.path = tail

    def __repr__(self):
        return 'open ' + str(self.path) + ';'
