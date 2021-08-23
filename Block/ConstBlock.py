<<<<<<< HEAD
from Block.BaseBlock import BaseBlock


class ConstBlock(BaseBlock):
    pass
=======
from Antlrtest import testParser
from Block.BaseBlock import BaseBlock
from Decl.ConstDecl import ConstDecl


class ConstBlock(BaseBlock):

    constDeclList = []

    def __init__(self, ctx:testParser.testParser.Const_blockContext):
        # if len(ctx.children) & 1:
        self.Build(ctx)
        # print(ctx.children[1].children[3])
        # print(type(ctx.children[1].children[3]))
        # else:
        #     print("OpenPackageBlock::error")

    def Build(self, ctx:testParser.testParser.Const_blockContext):
        self.constDeclList.clear()
        length = len(ctx.children)//2
        for i in range(length):
            constCtx = ctx.children[i*2+1]
            constDecl = ConstDecl(constCtx)
            self.constDeclList.append(constDecl)


    def __repr__(self):
        return 'open ' + str(self.path) + ';'


>>>>>>> 1019c1cd9a1955b7918d9526fcbec2bdc9039439
