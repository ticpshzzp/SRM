from enum import Enum

from Expr.ExprElement import ExprElement


class TypeExpr(ExprElement):

    class Form(Enum):
        UNK = 0
        BOOL = 1
        CHAR = 2
        FLOAT32 = 3
        FLOAT64 = 4
        INT8 = 5
        INT16 = 6
        INT32 = 7
        INT64 = 8
        UINT8 = 9
        UINT16 = 10
        UINT32 = 11
        UINT64 = 12

    typeEnum = Form.UNK

    typeDictSToI = {}
    typeDictIToS = ['UNK', 'BOOL', 'CHAR', 'FLOAT32', 'FLOAT64', 'INT8', 'INT16', 'INT32', 'INT64', 'UINT8', 'UINT16', 'UINT32', 'UINT64']

    def __init__(self, type):
        if type == 'int32':
            self.typeEnum = self.Form.INT32
        if type == 'int16':
            self.typeEnum = self.Form.INT16
        if type == 'float32':
            self.typeEnum = self.Form.FLOAT32



    '''
        输出格式化
    '''
    def __repr__(self):
        # if self.typeEnum == self.Form.
        return self.typeDictIToS[self.typeEnum.value]
        # rst = str(self.mVar)
        # if str(self.mTail) != '':
        #     rst += "--" + str(self.mTail)
        # return rst


# print(Form.BOOL.value)