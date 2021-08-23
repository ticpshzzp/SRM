from Decl.Decl import Decl
from Antlrtest import testParser



class ConstDecl(Decl):

    mInterfaceStatus = None
    mID = None
    mTypeExpr = None
    mExpr = None


    def __init__(self, ctx:testParser.testParser.Const_declContext):
        self.Build(ctx)



    def Build(self, ctx:testParser.testParser.Const_declContext):
        # for ct in ctx.children:
        #     print(type(ct))
        self.mInterfaceStatus = (ctx.children[0])

        self.mID = str(ctx.children[1])

        (ctx.children[3])

        # if len(ctx.children) == 6:
        #     self.mExpr = ExprElement(ctx.children[5])

