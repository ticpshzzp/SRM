from antlr4 import *
from antlr4.InputStream import InputStream

from Block.BlockImport import *
# from Block.OpenPackageBlock import OpenPackageBlock
<<<<<<< HEAD
=======
from Block.ConstBlock import ConstBlock
>>>>>>> 1019c1cd9a1955b7918d9526fcbec2bdc9039439
from testLexer import testLexer
from testParser import testParser


if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     input_stream = FileStream(sys.argv[1])
    # else:
    #     input_stream = InputStream(sys.stdin.readline())

    input_stream = FileStream('test_input1.txt')

    lexer = testLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = testParser(token_stream)
<<<<<<< HEAD
    tree = parser.decls()

    # print(tree.children[0])
    # print(tree.children[0].children[3])
=======
    tree = parser.expr()

    # print(tree.children[0])
    # print(tree.children[1])
    # print(type(tree.children[0]))
    # print(type(tree.children[1]))
    # print(type(tree))
    # print(tree.children[0])
    # print(tree.children[1])
>>>>>>> 1019c1cd9a1955b7918d9526fcbec2bdc9039439
    # print(type(tree.children[0]))
    # print(type(tree.children[1]))
    # print(type(tree))


    # opb = OpenPackageBlock(tree.children[1])
    # print(opb)

<<<<<<< HEAD
=======
    # ConstBlock(tree.children[0]);
    # print(tree.getRuleContext())
    # print(tree.getText())
    # print(tree.getRuleIndex())
    # print(tree.getSourceInterval())
    # print(tree.getTokens(134))
    # print(tree.children[0].getText())
    # tree.toStringTree()
    print(tree.list_expr())
    print(tree.id_expr().toStringTree(recog=parser))
>>>>>>> 1019c1cd9a1955b7918d9526fcbec2bdc9039439

    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)

