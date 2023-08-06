
import ipdb
from typecube import core as tlcore
from typecube.core import Expr
from typecube.annotations import Annotatable
from typecube import unifier as tlunifier
from typecube.utils import FieldPath

BooleanType = tlcore.make_literal_type("boolean")
ByteType = tlcore.make_literal_type("byte")
IntType = tlcore.make_literal_type("int")
LongType = tlcore.make_literal_type("long")
FloatType = tlcore.make_literal_type("float")
DoubleType = tlcore.make_literal_type("double")
StringType = tlcore.make_literal_type("string")
MapType = tlcore.make_type_fun("map", ["K", "V"], None, None)
ListType = tlcore.make_type_fun("list", ["V"], None, None)

class NewExpr(Expr):
    """ An expression used to create instead of a type.  It can be passed values for its child arguments.
    This is just another shortcut for a function appication of a specific kind.
    """
    def __init__(self, objtype, **arg_values):
        self.objtype = objtype
        self.arg_values = arg_values or {}

    def _evaltype(self):
        return self.objtype.resolve()

    def _resolve(self):
        resolved_objtype = self.objtype.resolve()
        resolved_args = {key: value.resolve() for key,value in self.arg_values.iteritems()}
        return self

class Assignment(Expr):
    def __init__(self, target_variable, expr):
        Expr.__init__(self)
        self.target_variable = target_variable
        self.expr = expr

    def _equals(self, another):
        return self.target_variable.equals(another.target_variable) and \
                self.expr.equals(another.expr)

    def _evaltype(self):
        resolved_expr = self.expr.resolve()
        return resolved_expr.evaltype()

    def _resolve(self):
        """
        Processes an exprs and resolves name bindings and creating new local vars 
        in the process if required.
        """
        # Resolve the target variable's binding.  This does'nt necessarily have
        # to evaluate types.
        # This will help us with type inference going backwards
        resolved_var = self.target_variable.resolve()

        # Resolve all types in child exprs.  
        # Apart from just evaluating all child exprs, also make sure
        # Resolve field paths that should come from source type
        resolved_expr = self.expr.resolve()
        return self

class Literal(Expr):
    """
    An expr that contains a literal value like a number, string, boolean, list, or map.
    """
    def __init__(self, value, value_type):
        Expr.__init__(self)
        self.value = value
        self.value_type = value_type

    def _equals(self, another):
        return self.value == another.value and self.value_type.equals(another.value_type)

    def _evaltype(self):
        return self.value_type

    def resolve(self, resolver):
        return self

    def __repr__(self):
        return "<Literal(0x%x), Value: %s>" % (id(self), str(self.value))

class ExprList(Expr):
    """ A list of statements. """
    def __init__(self, children = None):
        Expr.__init__(self)
        self.children = children or []

    def add(self, expr):
        if not issubclass(expr.__class__, Expr):
            ipdb.set_trace()
            assert issubclass(expr.__class__, Expr), "Cannot add non Expr instances to an ExprList"
        self.children.append(expr)

    def extend(self, another):
        if type(another) is ExprList:
            self.children.extend(another.children)
        else:
            self.add(another)

    def _evaltype(self):
        resolved = self.resolve()
        return resolved.children[-1].evaltype()

    def _resolve(self):
        resolved_exprs = [expr.resolve() for expr in self.children]
        if any(x != y for x,y in zip(self.children, resolved_exprs)):
            return ExprList(resolved_exprs)
        return self

class DictExpr(Expr):
    def __init__(self, keys, values):
        super(DictExpr, self).__init__()
        self.keys = keys
        self.values = values
        assert len(keys) == len(values)

    def _resolve(self):
        for key,value in izip(self.keys, self.values):
            key.resolve()
            value.resolve()

        # TODO - Unify the types of child exprs and find the tightest type here Damn It!!!
        return self

class ListExpr(Expr):
    def __init__(self, values):
        super(ListExpr, self).__init__()
        self.values = values

    def _evaltype(self):
        # TODO - Unify the types of child exprs and find the tightest type here Damn It!!!
        return ListType.apply(tlcore.AnyType)

    def _resolve(self):
        """
        Processes an exprs and resolves name bindings and creating new local vars 
        in the process if required.
        """
        resolved_exprs = [expr.resolve() for expr in self.values]
        if any(x != y for x,y in zip(self.values, resolved_exprs)):
            return ListExpr(resolved_exprs)
        return self

class TupleExpr(Expr):
    def __init__(self, values):
        super(TupleExpr, self).__init__()
        self.values = values or []

    def _evaltype(self):
        # TODO - Unify the types of child exprs and find the tightest type here Damn It!!!
        return ListType.apply(tlcore.AnyType)

    def _resolve(self):
        """
        Processes an exprs and resolves name bindings and creating new local vars 
        in the process if required.
        """
        resolved_exprs = [expr.resolve() for expr in self.values]
        if any(x != y for x,y in zip(self.values, resolved_exprs)):
            return TupleExpr(resolved_exprs)
        return self

class IfExpr(Expr):
    """ Conditional exprs are used to represent if-else exprs. """
    def __init__(self, cases, default_expr):
        super(IfExpr, self).__init__()
        self.cases = cases or []
        self.default_expr = default_expr or []

    def __repr__(self):
        return "<IfExp - ID: 0x%x>" % (id(self))

    def set_evaluated_typeexpr(self, vartype):
        assert False, "cannot set evaluated type of an If expr (yet)"

    def _resolve(self):
        """ Resolves bindings and types in all child exprs. """
        ipdb.set_trace()
        assert self._evaluated_typeexpr == None, "Type has already been resolved, should not have been called twice."

        for condition, expr in self.cases:
            condition.resolve()
            expr.resolve()

        if self.default_expr: self.default_expr.resolve()

        # TODO: Return a union type instead
        self._evaluated_typeexpr = tlcore.VoidType
        return self
