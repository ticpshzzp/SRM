from antlr4 import *
from antlr4.InputStream import InputStream

from Block.BlockImport import *
# from Block.OpenPackageBlock import OpenPackageBlock
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
    tree = parser.decls()

    # print(tree.children[0])
    # print(tree.children[0].children[3])
    # print(type(tree.children[0]))
    # print(type(tree.children[1]))
    # print(type(tree))


    # opb = OpenPackageBlock(tree.children[1])
    # print(opb)


    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)

