from Expr.ExprElement import ExprElement
from Antlrtest.testParser import testParser


class ExprFactory():

    mExpr = ExprElement(None)

    def CreateExpr(self, ctx:testParser.ExprContext):
        length = len(ctx.children)
        if length == 1:
            if ctx.id_expr() is not None:
                pass
            elif ctx.atom() is not None:
                pass
            elif ctx.list_expr() is not None:
                pass
            elif ctx.tempo_expr() is not None:
                pass
            elif ctx.bool_expr() is not None:
                pass
            elif ctx.arith_expr() is not None:
                pass
            elif ctx.array_expr() is not None:
                pass
            elif ctx.struct_expr() is not None:
                pass
            elif ctx.mixed_constructor() is not None:
                pass
            elif ctx.switch_expr() is not None:
                pass
            elif ctx.apply_expr() is not None:
                pass
        else:
            pass




        return self.mExpr
