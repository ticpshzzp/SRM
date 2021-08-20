# Generated from test.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .testParser import testParser
else:
    from testParser import testParser

# This class defines a complete listener for a parse tree produced by testParser.
class testListener(ParseTreeListener):

    # Enter a parse tree produced by testParser#program.
    def enterProgram(self, ctx:testParser.ProgramContext):
        pass

    # Exit a parse tree produced by testParser#program.
    def exitProgram(self, ctx:testParser.ProgramContext):
        pass


    # Enter a parse tree produced by testParser#decls.
    def enterDecls(self, ctx:testParser.DeclsContext):
        pass

    # Exit a parse tree produced by testParser#decls.
    def exitDecls(self, ctx:testParser.DeclsContext):
        pass


    # Enter a parse tree produced by testParser#path.
    def enterPath(self, ctx:testParser.PathContext):
        pass

    # Exit a parse tree produced by testParser#path.
    def exitPath(self, ctx:testParser.PathContext):
        pass


    # Enter a parse tree produced by testParser#path_id.
    def enterPath_id(self, ctx:testParser.Path_idContext):
        pass

    # Exit a parse tree produced by testParser#path_id.
    def exitPath_id(self, ctx:testParser.Path_idContext):
        pass


    # Enter a parse tree produced by testParser#package_decl.
    def enterPackage_decl(self, ctx:testParser.Package_declContext):
        pass

    # Exit a parse tree produced by testParser#package_decl.
    def exitPackage_decl(self, ctx:testParser.Package_declContext):
        pass


    # Enter a parse tree produced by testParser#visibility.
    def enterVisibility(self, ctx:testParser.VisibilityContext):
        pass

    # Exit a parse tree produced by testParser#visibility.
    def exitVisibility(self, ctx:testParser.VisibilityContext):
        pass


    # Enter a parse tree produced by testParser#external.
    def enterExternal(self, ctx:testParser.ExternalContext):
        pass

    # Exit a parse tree produced by testParser#external.
    def exitExternal(self, ctx:testParser.ExternalContext):
        pass


    # Enter a parse tree produced by testParser#interface_status.
    def enterInterface_status(self, ctx:testParser.Interface_statusContext):
        pass

    # Exit a parse tree produced by testParser#interface_status.
    def exitInterface_status(self, ctx:testParser.Interface_statusContext):
        pass


    # Enter a parse tree produced by testParser#type_block.
    def enterType_block(self, ctx:testParser.Type_blockContext):
        pass

    # Exit a parse tree produced by testParser#type_block.
    def exitType_block(self, ctx:testParser.Type_blockContext):
        pass


    # Enter a parse tree produced by testParser#type_decl.
    def enterType_decl(self, ctx:testParser.Type_declContext):
        pass

    # Exit a parse tree produced by testParser#type_decl.
    def exitType_decl(self, ctx:testParser.Type_declContext):
        pass


    # Enter a parse tree produced by testParser#numeric_kind.
    def enterNumeric_kind(self, ctx:testParser.Numeric_kindContext):
        pass

    # Exit a parse tree produced by testParser#numeric_kind.
    def exitNumeric_kind(self, ctx:testParser.Numeric_kindContext):
        pass


    # Enter a parse tree produced by testParser#numeric.
    def enterNumeric(self, ctx:testParser.NumericContext):
        pass

    # Exit a parse tree produced by testParser#numeric.
    def exitNumeric(self, ctx:testParser.NumericContext):
        pass


    # Enter a parse tree produced by testParser#myint.
    def enterMyint(self, ctx:testParser.MyintContext):
        pass

    # Exit a parse tree produced by testParser#myint.
    def exitMyint(self, ctx:testParser.MyintContext):
        pass


    # Enter a parse tree produced by testParser#myfloat.
    def enterMyfloat(self, ctx:testParser.MyfloatContext):
        pass

    # Exit a parse tree produced by testParser#myfloat.
    def exitMyfloat(self, ctx:testParser.MyfloatContext):
        pass


    # Enter a parse tree produced by testParser#signed.
    def enterSigned(self, ctx:testParser.SignedContext):
        pass

    # Exit a parse tree produced by testParser#signed.
    def exitSigned(self, ctx:testParser.SignedContext):
        pass


    # Enter a parse tree produced by testParser#unsigned.
    def enterUnsigned(self, ctx:testParser.UnsignedContext):
        pass

    # Exit a parse tree produced by testParser#unsigned.
    def exitUnsigned(self, ctx:testParser.UnsignedContext):
        pass


    # Enter a parse tree produced by testParser#type_def.
    def enterType_def(self, ctx:testParser.Type_defContext):
        pass

    # Exit a parse tree produced by testParser#type_def.
    def exitType_def(self, ctx:testParser.Type_defContext):
        pass


    # Enter a parse tree produced by testParser#type_expr.
    def enterType_expr(self, ctx:testParser.Type_exprContext):
        pass

    # Exit a parse tree produced by testParser#type_expr.
    def exitType_expr(self, ctx:testParser.Type_exprContext):
        pass


    # Enter a parse tree produced by testParser#field_decl.
    def enterField_decl(self, ctx:testParser.Field_declContext):
        pass

    # Exit a parse tree produced by testParser#field_decl.
    def exitField_decl(self, ctx:testParser.Field_declContext):
        pass


    # Enter a parse tree produced by testParser#typevar.
    def enterTypevar(self, ctx:testParser.TypevarContext):
        pass

    # Exit a parse tree produced by testParser#typevar.
    def exitTypevar(self, ctx:testParser.TypevarContext):
        pass


    # Enter a parse tree produced by testParser#group_block.
    def enterGroup_block(self, ctx:testParser.Group_blockContext):
        pass

    # Exit a parse tree produced by testParser#group_block.
    def exitGroup_block(self, ctx:testParser.Group_blockContext):
        pass


    # Enter a parse tree produced by testParser#group_decl.
    def enterGroup_decl(self, ctx:testParser.Group_declContext):
        pass

    # Exit a parse tree produced by testParser#group_decl.
    def exitGroup_decl(self, ctx:testParser.Group_declContext):
        pass


    # Enter a parse tree produced by testParser#group_expr.
    def enterGroup_expr(self, ctx:testParser.Group_exprContext):
        pass

    # Exit a parse tree produced by testParser#group_expr.
    def exitGroup_expr(self, ctx:testParser.Group_exprContext):
        pass


    # Enter a parse tree produced by testParser#const_block.
    def enterConst_block(self, ctx:testParser.Const_blockContext):
        pass

    # Exit a parse tree produced by testParser#const_block.
    def exitConst_block(self, ctx:testParser.Const_blockContext):
        pass


    # Enter a parse tree produced by testParser#const_decl.
    def enterConst_decl(self, ctx:testParser.Const_declContext):
        pass

    # Exit a parse tree produced by testParser#const_decl.
    def exitConst_decl(self, ctx:testParser.Const_declContext):
        pass


    # Enter a parse tree produced by testParser#sensor_block.
    def enterSensor_block(self, ctx:testParser.Sensor_blockContext):
        pass

    # Exit a parse tree produced by testParser#sensor_block.
    def exitSensor_block(self, ctx:testParser.Sensor_blockContext):
        pass


    # Enter a parse tree produced by testParser#sensor_decl.
    def enterSensor_decl(self, ctx:testParser.Sensor_declContext):
        pass

    # Exit a parse tree produced by testParser#sensor_decl.
    def exitSensor_decl(self, ctx:testParser.Sensor_declContext):
        pass


    # Enter a parse tree produced by testParser#var_decls.
    def enterVar_decls(self, ctx:testParser.Var_declsContext):
        pass

    # Exit a parse tree produced by testParser#var_decls.
    def exitVar_decls(self, ctx:testParser.Var_declsContext):
        pass


    # Enter a parse tree produced by testParser#var_id.
    def enterVar_id(self, ctx:testParser.Var_idContext):
        pass

    # Exit a parse tree produced by testParser#var_id.
    def exitVar_id(self, ctx:testParser.Var_idContext):
        pass


    # Enter a parse tree produced by testParser#when_decl.
    def enterWhen_decl(self, ctx:testParser.When_declContext):
        pass

    # Exit a parse tree produced by testParser#when_decl.
    def exitWhen_decl(self, ctx:testParser.When_declContext):
        pass


    # Enter a parse tree produced by testParser#default_decl.
    def enterDefault_decl(self, ctx:testParser.Default_declContext):
        pass

    # Exit a parse tree produced by testParser#default_decl.
    def exitDefault_decl(self, ctx:testParser.Default_declContext):
        pass


    # Enter a parse tree produced by testParser#last_decl.
    def enterLast_decl(self, ctx:testParser.Last_declContext):
        pass

    # Exit a parse tree produced by testParser#last_decl.
    def exitLast_decl(self, ctx:testParser.Last_declContext):
        pass


    # Enter a parse tree produced by testParser#user_op_decl.
    def enterUser_op_decl(self, ctx:testParser.User_op_declContext):
        pass

    # Exit a parse tree produced by testParser#user_op_decl.
    def exitUser_op_decl(self, ctx:testParser.User_op_declContext):
        pass


    # Enter a parse tree produced by testParser#op_kind.
    def enterOp_kind(self, ctx:testParser.Op_kindContext):
        pass

    # Exit a parse tree produced by testParser#op_kind.
    def exitOp_kind(self, ctx:testParser.Op_kindContext):
        pass


    # Enter a parse tree produced by testParser#size_decl.
    def enterSize_decl(self, ctx:testParser.Size_declContext):
        pass

    # Exit a parse tree produced by testParser#size_decl.
    def exitSize_decl(self, ctx:testParser.Size_declContext):
        pass


    # Enter a parse tree produced by testParser#params.
    def enterParams(self, ctx:testParser.ParamsContext):
        pass

    # Exit a parse tree produced by testParser#params.
    def exitParams(self, ctx:testParser.ParamsContext):
        pass


    # Enter a parse tree produced by testParser#where_decl.
    def enterWhere_decl(self, ctx:testParser.Where_declContext):
        pass

    # Exit a parse tree produced by testParser#where_decl.
    def exitWhere_decl(self, ctx:testParser.Where_declContext):
        pass


    # Enter a parse tree produced by testParser#spec_decl.
    def enterSpec_decl(self, ctx:testParser.Spec_declContext):
        pass

    # Exit a parse tree produced by testParser#spec_decl.
    def exitSpec_decl(self, ctx:testParser.Spec_declContext):
        pass


    # Enter a parse tree produced by testParser#opt_body.
    def enterOpt_body(self, ctx:testParser.Opt_bodyContext):
        pass

    # Exit a parse tree produced by testParser#opt_body.
    def exitOpt_body(self, ctx:testParser.Opt_bodyContext):
        pass


    # Enter a parse tree produced by testParser#data_def.
    def enterData_def(self, ctx:testParser.Data_defContext):
        pass

    # Exit a parse tree produced by testParser#data_def.
    def exitData_def(self, ctx:testParser.Data_defContext):
        pass


    # Enter a parse tree produced by testParser#scope.
    def enterScope(self, ctx:testParser.ScopeContext):
        pass

    # Exit a parse tree produced by testParser#scope.
    def exitScope(self, ctx:testParser.ScopeContext):
        pass


    # Enter a parse tree produced by testParser#signal_block.
    def enterSignal_block(self, ctx:testParser.Signal_blockContext):
        pass

    # Exit a parse tree produced by testParser#signal_block.
    def exitSignal_block(self, ctx:testParser.Signal_blockContext):
        pass


    # Enter a parse tree produced by testParser#local_block.
    def enterLocal_block(self, ctx:testParser.Local_blockContext):
        pass

    # Exit a parse tree produced by testParser#local_block.
    def exitLocal_block(self, ctx:testParser.Local_blockContext):
        pass


    # Enter a parse tree produced by testParser#eqs.
    def enterEqs(self, ctx:testParser.EqsContext):
        pass

    # Exit a parse tree produced by testParser#eqs.
    def exitEqs(self, ctx:testParser.EqsContext):
        pass


    # Enter a parse tree produced by testParser#equation.
    def enterEquation(self, ctx:testParser.EquationContext):
        pass

    # Exit a parse tree produced by testParser#equation.
    def exitEquation(self, ctx:testParser.EquationContext):
        pass


    # Enter a parse tree produced by testParser#simple_equation.
    def enterSimple_equation(self, ctx:testParser.Simple_equationContext):
        pass

    # Exit a parse tree produced by testParser#simple_equation.
    def exitSimple_equation(self, ctx:testParser.Simple_equationContext):
        pass


    # Enter a parse tree produced by testParser#lhs.
    def enterLhs(self, ctx:testParser.LhsContext):
        pass

    # Exit a parse tree produced by testParser#lhs.
    def exitLhs(self, ctx:testParser.LhsContext):
        pass


    # Enter a parse tree produced by testParser#lhs_id.
    def enterLhs_id(self, ctx:testParser.Lhs_idContext):
        pass

    # Exit a parse tree produced by testParser#lhs_id.
    def exitLhs_id(self, ctx:testParser.Lhs_idContext):
        pass


    # Enter a parse tree produced by testParser#myassert.
    def enterMyassert(self, ctx:testParser.MyassertContext):
        pass

    # Exit a parse tree produced by testParser#myassert.
    def exitMyassert(self, ctx:testParser.MyassertContext):
        pass


    # Enter a parse tree produced by testParser#control_block.
    def enterControl_block(self, ctx:testParser.Control_blockContext):
        pass

    # Exit a parse tree produced by testParser#control_block.
    def exitControl_block(self, ctx:testParser.Control_blockContext):
        pass


    # Enter a parse tree produced by testParser#emission.
    def enterEmission(self, ctx:testParser.EmissionContext):
        pass

    # Exit a parse tree produced by testParser#emission.
    def exitEmission(self, ctx:testParser.EmissionContext):
        pass


    # Enter a parse tree produced by testParser#emission_body.
    def enterEmission_body(self, ctx:testParser.Emission_bodyContext):
        pass

    # Exit a parse tree produced by testParser#emission_body.
    def exitEmission_body(self, ctx:testParser.Emission_bodyContext):
        pass


    # Enter a parse tree produced by testParser#myreturn.
    def enterMyreturn(self, ctx:testParser.MyreturnContext):
        pass

    # Exit a parse tree produced by testParser#myreturn.
    def exitMyreturn(self, ctx:testParser.MyreturnContext):
        pass


    # Enter a parse tree produced by testParser#returns_var.
    def enterReturns_var(self, ctx:testParser.Returns_varContext):
        pass

    # Exit a parse tree produced by testParser#returns_var.
    def exitReturns_var(self, ctx:testParser.Returns_varContext):
        pass


    # Enter a parse tree produced by testParser#clocked_block.
    def enterClocked_block(self, ctx:testParser.Clocked_blockContext):
        pass

    # Exit a parse tree produced by testParser#clocked_block.
    def exitClocked_block(self, ctx:testParser.Clocked_blockContext):
        pass


    # Enter a parse tree produced by testParser#if_block.
    def enterIf_block(self, ctx:testParser.If_blockContext):
        pass

    # Exit a parse tree produced by testParser#if_block.
    def exitIf_block(self, ctx:testParser.If_blockContext):
        pass


    # Enter a parse tree produced by testParser#match_block.
    def enterMatch_block(self, ctx:testParser.Match_blockContext):
        pass

    # Exit a parse tree produced by testParser#match_block.
    def exitMatch_block(self, ctx:testParser.Match_blockContext):
        pass


    # Enter a parse tree produced by testParser#state_machine.
    def enterState_machine(self, ctx:testParser.State_machineContext):
        pass

    # Exit a parse tree produced by testParser#state_machine.
    def exitState_machine(self, ctx:testParser.State_machineContext):
        pass


    # Enter a parse tree produced by testParser#state_decl.
    def enterState_decl(self, ctx:testParser.State_declContext):
        pass

    # Exit a parse tree produced by testParser#state_decl.
    def exitState_decl(self, ctx:testParser.State_declContext):
        pass


    # Enter a parse tree produced by testParser#transition.
    def enterTransition(self, ctx:testParser.TransitionContext):
        pass

    # Exit a parse tree produced by testParser#transition.
    def exitTransition(self, ctx:testParser.TransitionContext):
        pass


    # Enter a parse tree produced by testParser#arrow.
    def enterArrow(self, ctx:testParser.ArrowContext):
        pass

    # Exit a parse tree produced by testParser#arrow.
    def exitArrow(self, ctx:testParser.ArrowContext):
        pass


    # Enter a parse tree produced by testParser#fork.
    def enterFork(self, ctx:testParser.ForkContext):
        pass

    # Exit a parse tree produced by testParser#fork.
    def exitFork(self, ctx:testParser.ForkContext):
        pass


    # Enter a parse tree produced by testParser#elif_fork.
    def enterElif_fork(self, ctx:testParser.Elif_forkContext):
        pass

    # Exit a parse tree produced by testParser#elif_fork.
    def exitElif_fork(self, ctx:testParser.Elif_forkContext):
        pass


    # Enter a parse tree produced by testParser#else_fork.
    def enterElse_fork(self, ctx:testParser.Else_forkContext):
        pass

    # Exit a parse tree produced by testParser#else_fork.
    def exitElse_fork(self, ctx:testParser.Else_forkContext):
        pass


    # Enter a parse tree produced by testParser#target.
    def enterTarget(self, ctx:testParser.TargetContext):
        pass

    # Exit a parse tree produced by testParser#target.
    def exitTarget(self, ctx:testParser.TargetContext):
        pass


    # Enter a parse tree produced by testParser#actions.
    def enterActions(self, ctx:testParser.ActionsContext):
        pass

    # Exit a parse tree produced by testParser#actions.
    def exitActions(self, ctx:testParser.ActionsContext):
        pass


    # Enter a parse tree produced by testParser#clock_expr.
    def enterClock_expr(self, ctx:testParser.Clock_exprContext):
        pass

    # Exit a parse tree produced by testParser#clock_expr.
    def exitClock_expr(self, ctx:testParser.Clock_exprContext):
        pass


    # Enter a parse tree produced by testParser#expr.
    def enterExpr(self, ctx:testParser.ExprContext):
        pass

    # Exit a parse tree produced by testParser#expr.
    def exitExpr(self, ctx:testParser.ExprContext):
        pass


    # Enter a parse tree produced by testParser#atom.
    def enterAtom(self, ctx:testParser.AtomContext):
        pass

    # Exit a parse tree produced by testParser#atom.
    def exitAtom(self, ctx:testParser.AtomContext):
        pass


    # Enter a parse tree produced by testParser#id_expr.
    def enterId_expr(self, ctx:testParser.Id_exprContext):
        pass

    # Exit a parse tree produced by testParser#id_expr.
    def exitId_expr(self, ctx:testParser.Id_exprContext):
        pass


    # Enter a parse tree produced by testParser#list_expr.
    def enterList_expr(self, ctx:testParser.List_exprContext):
        pass

    # Exit a parse tree produced by testParser#list_expr.
    def exitList_expr(self, ctx:testParser.List_exprContext):
        pass


    # Enter a parse tree produced by testParser#mylist.
    def enterMylist(self, ctx:testParser.MylistContext):
        pass

    # Exit a parse tree produced by testParser#mylist.
    def exitMylist(self, ctx:testParser.MylistContext):
        pass


    # Enter a parse tree produced by testParser#tempo_expr.
    def enterTempo_expr(self, ctx:testParser.Tempo_exprContext):
        pass

    # Exit a parse tree produced by testParser#tempo_expr.
    def exitTempo_expr(self, ctx:testParser.Tempo_exprContext):
        pass


    # Enter a parse tree produced by testParser#arith_expr.
    def enterArith_expr(self, ctx:testParser.Arith_exprContext):
        pass

    # Exit a parse tree produced by testParser#arith_expr.
    def exitArith_expr(self, ctx:testParser.Arith_exprContext):
        pass


    # Enter a parse tree produced by testParser#unary_arith_op.
    def enterUnary_arith_op(self, ctx:testParser.Unary_arith_opContext):
        pass

    # Exit a parse tree produced by testParser#unary_arith_op.
    def exitUnary_arith_op(self, ctx:testParser.Unary_arith_opContext):
        pass


    # Enter a parse tree produced by testParser#bin_arith_op.
    def enterBin_arith_op(self, ctx:testParser.Bin_arith_opContext):
        pass

    # Exit a parse tree produced by testParser#bin_arith_op.
    def exitBin_arith_op(self, ctx:testParser.Bin_arith_opContext):
        pass


    # Enter a parse tree produced by testParser#relation_expr.
    def enterRelation_expr(self, ctx:testParser.Relation_exprContext):
        pass

    # Exit a parse tree produced by testParser#relation_expr.
    def exitRelation_expr(self, ctx:testParser.Relation_exprContext):
        pass


    # Enter a parse tree produced by testParser#bin_relation_op.
    def enterBin_relation_op(self, ctx:testParser.Bin_relation_opContext):
        pass

    # Exit a parse tree produced by testParser#bin_relation_op.
    def exitBin_relation_op(self, ctx:testParser.Bin_relation_opContext):
        pass


    # Enter a parse tree produced by testParser#bool_expr.
    def enterBool_expr(self, ctx:testParser.Bool_exprContext):
        pass

    # Exit a parse tree produced by testParser#bool_expr.
    def exitBool_expr(self, ctx:testParser.Bool_exprContext):
        pass


    # Enter a parse tree produced by testParser#bin_bool_op.
    def enterBin_bool_op(self, ctx:testParser.Bin_bool_opContext):
        pass

    # Exit a parse tree produced by testParser#bin_bool_op.
    def exitBin_bool_op(self, ctx:testParser.Bin_bool_opContext):
        pass


    # Enter a parse tree produced by testParser#bin_op.
    def enterBin_op(self, ctx:testParser.Bin_opContext):
        pass

    # Exit a parse tree produced by testParser#bin_op.
    def exitBin_op(self, ctx:testParser.Bin_opContext):
        pass


    # Enter a parse tree produced by testParser#array_expr.
    def enterArray_expr(self, ctx:testParser.Array_exprContext):
        pass

    # Exit a parse tree produced by testParser#array_expr.
    def exitArray_expr(self, ctx:testParser.Array_exprContext):
        pass


    # Enter a parse tree produced by testParser#struct_expr.
    def enterStruct_expr(self, ctx:testParser.Struct_exprContext):
        pass

    # Exit a parse tree produced by testParser#struct_expr.
    def exitStruct_expr(self, ctx:testParser.Struct_exprContext):
        pass


    # Enter a parse tree produced by testParser#mixed_constructor.
    def enterMixed_constructor(self, ctx:testParser.Mixed_constructorContext):
        pass

    # Exit a parse tree produced by testParser#mixed_constructor.
    def exitMixed_constructor(self, ctx:testParser.Mixed_constructorContext):
        pass


    # Enter a parse tree produced by testParser#label_expr.
    def enterLabel_expr(self, ctx:testParser.Label_exprContext):
        pass

    # Exit a parse tree produced by testParser#label_expr.
    def exitLabel_expr(self, ctx:testParser.Label_exprContext):
        pass


    # Enter a parse tree produced by testParser#index.
    def enterIndex(self, ctx:testParser.IndexContext):
        pass

    # Exit a parse tree produced by testParser#index.
    def exitIndex(self, ctx:testParser.IndexContext):
        pass


    # Enter a parse tree produced by testParser#label_or_index.
    def enterLabel_or_index(self, ctx:testParser.Label_or_indexContext):
        pass

    # Exit a parse tree produced by testParser#label_or_index.
    def exitLabel_or_index(self, ctx:testParser.Label_or_indexContext):
        pass


    # Enter a parse tree produced by testParser#switch_expr.
    def enterSwitch_expr(self, ctx:testParser.Switch_exprContext):
        pass

    # Exit a parse tree produced by testParser#switch_expr.
    def exitSwitch_expr(self, ctx:testParser.Switch_exprContext):
        pass


    # Enter a parse tree produced by testParser#case_expr.
    def enterCase_expr(self, ctx:testParser.Case_exprContext):
        pass

    # Exit a parse tree produced by testParser#case_expr.
    def exitCase_expr(self, ctx:testParser.Case_exprContext):
        pass


    # Enter a parse tree produced by testParser#pattern.
    def enterPattern(self, ctx:testParser.PatternContext):
        pass

    # Exit a parse tree produced by testParser#pattern.
    def exitPattern(self, ctx:testParser.PatternContext):
        pass


    # Enter a parse tree produced by testParser#apply_expr.
    def enterApply_expr(self, ctx:testParser.Apply_exprContext):
        pass

    # Exit a parse tree produced by testParser#apply_expr.
    def exitApply_expr(self, ctx:testParser.Apply_exprContext):
        pass


    # Enter a parse tree produced by testParser#operator.
    def enterOperator(self, ctx:testParser.OperatorContext):
        pass

    # Exit a parse tree produced by testParser#operator.
    def exitOperator(self, ctx:testParser.OperatorContext):
        pass


    # Enter a parse tree produced by testParser#prefix.
    def enterPrefix(self, ctx:testParser.PrefixContext):
        pass

    # Exit a parse tree produced by testParser#prefix.
    def exitPrefix(self, ctx:testParser.PrefixContext):
        pass


    # Enter a parse tree produced by testParser#iterator.
    def enterIterator(self, ctx:testParser.IteratorContext):
        pass

    # Exit a parse tree produced by testParser#iterator.
    def exitIterator(self, ctx:testParser.IteratorContext):
        pass


    # Enter a parse tree produced by testParser#iterator_mw.
    def enterIterator_mw(self, ctx:testParser.Iterator_mwContext):
        pass

    # Exit a parse tree produced by testParser#iterator_mw.
    def exitIterator_mw(self, ctx:testParser.Iterator_mwContext):
        pass


    # Enter a parse tree produced by testParser#boolean.
    def enterBoolean(self, ctx:testParser.BooleanContext):
        pass

    # Exit a parse tree produced by testParser#boolean.
    def exitBoolean(self, ctx:testParser.BooleanContext):
        pass


    # Enter a parse tree produced by testParser#integer.
    def enterInteger(self, ctx:testParser.IntegerContext):
        pass

    # Exit a parse tree produced by testParser#integer.
    def exitInteger(self, ctx:testParser.IntegerContext):
        pass


    # Enter a parse tree produced by testParser#character.
    def enterCharacter(self, ctx:testParser.CharacterContext):
        pass

    # Exit a parse tree produced by testParser#character.
    def exitCharacter(self, ctx:testParser.CharacterContext):
        pass



del testParser