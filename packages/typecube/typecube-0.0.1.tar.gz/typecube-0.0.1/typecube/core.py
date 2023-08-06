
from enum import Enum
from ipdb import set_trace
from collections import defaultdict
from itertools import izip
from typecube import errors
from typecube.utils import FieldPath
from typecube.annotations import Annotatable

def istype(t): return issubclass(t.__class__, Type)

class NameResolver(object):
    def resolve_name(self, name, condition = None):
        """ Tries to resolve a name in this expression. """
        value = self._resolve_name(name, condition)
        if value and (condition is None or condition(value)):
            return value
        if self.parent:     # Try the parent expression
            return self.parent.resolve_name(name, condition)
        raise errors.TLException("Unable to resolve name: %s" % name)

class Expr(NameResolver):
    """
    Parent of all exprs.  All exprs must have a value.  Exprs only appear in functions.
    """
    def __init__(self, parent = None):
        self._parent = parent

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        if self._parent is not None and value != self._parent:
            set_trace()
        oldvalue = self._parent
        self._parent = value
        self.parent_changed(oldvalue)

    def parent_changed(self, oldvalue):
        pass

    #########
    def ensure_parents(self):
        """ Ensures that all children have the parents setup correctly.  
        Assumes that the parent of this expression is set corrected before this is called.
        """
        assert self.parent is not None
        pass

    def resolve_name(self, name, condition = None):
        if self.parent is None:
            set_trace()
            assert self.parent is not None, "Parent of %s is None" % type(self)
        return NameResolver.resolve_name(self, name, condition)

    def _resolve_name(self, name, condition = None):
        return None

    def equals(self, another):
        return isinstance(another, self.__class__) and self._equals(another)

    def _equals(self, another):
        assert False, "Not Implemented"

    def evaltype(self):
        # Do caching of results here based on resolver!
        return self._evaltype()

    def _evaltype(self):
        set_trace()
        assert False, "not implemented"
        return None

    def resolve(self):
        # Do caching of results here based on resolver!
        return self._resolve()

    def _resolve(self):
        """ This method resolves a type expr to a type object. 
        The resolver is used to get bindings for names used in this expr.
        
        Returns a ResolvedValue object that contains the final expr value after resolution of this expr.
        """
        assert False, "Not Implemented"
        return self

class Var(Expr):
    """ An occurence of a name that can be bound to a value, a field or a type. """
    def __init__(self, field_path):
        super(Var, self).__init__()
        if type(field_path) in (str, unicode):
            field_path = FieldPath(field_path)
        self.field_path = field_path
        assert type(field_path) is FieldPath and field_path.length > 0

    def _equals(self, another):
        return self.field_path.parts == another.field_path.parts

    def __repr__(self):
        return "<VarExp - ID: 0x%x, Value: %s>" % (id(self), str(self.field_path))

    def _evaltype(self):
        resolved = self.resolve()
        if type(resolved) is Type:
            set_trace()
            return resolved
        if type(resolved) is Fun:
            return resolved.fun_type.resolve()
        if issubclass(resolved.__class__, FunApp):
            func = resolved.func_expr.resolve()
            fun_type = func.fun_type.resolve()
            return fun_type.output_typearg
        if issubclass(resolved.__class__, Expr):
            return resolved.evaltype()
        set_trace()
        assert False, "Unknown resolved value type"

    def _resolve(self):
        """
        Returns the actual entry pointed to by the "first" part of the field path.
        """
        first = self.field_path.get(0)
        target = self.resolve_name(first)
        if target is None:
            assert target is not None, "Could not resolve '%s'" % first
        return target

class Fun(Expr, Annotatable):
    """
    Defines a function binding along with the mappings to each of the 
    specific backends.
    """
    def __init__(self, fqn, fun_type, expr, parent, annotations = None, docs = ""):
        Expr.__init__(self, parent)
        Annotatable.__init__(self, annotations, docs)
        self.fqn = fqn
        self.fun_type = fun_type
        self.fun_type.parent = self.parent
        self.expr = expr
        if self.expr:
            self.expr.parent = self
        self.temp_variables = {}

    def _equals(self, another):
        return self.fqn == another.fqn and \
                self.fun_type.equals(another.fun_type) and \
                self.expr.equals(another.expr)

    @property
    def name(self):
        return self.fqn.split(".")[-1]

    def __json__(self, **kwargs):
        out = {}
        if self.fqn:
            out["fqn"] = self.fqn
        if kwargs.get("include_docs", False) and self.docs:
            out["docs"] = self.docs
        if self.fun_type:
            out["type"] = self.fun_type.json(**kwargs)
        return out

    @property
    def is_external(self): return self.expr is None

    def debug_show(self, level = 0):
        function = self
        print ("  " * (level)) + "SourceArgs:"
        for typearg in function.fun_type.args:
            print ("  " * (level + 1)) + ("%s: %s" % (typearg.name,typearg))

        print ("  " * (level)) + "OutputArg:"
        if function.fun_type.output_arg:
            print ("  " * (level + 1)) + "%s" % function.fun_type.output_arg

        print ("  " * (level)) + "Locals:"
        for key,value in self.temp_variables.iteritems():
            print ("  " * (level + 1)) + ("%s: %s" % (key, value))

    def _resolve_name(self, name, condition = None):
        """ Try to resolve a name to a local, source or destination variable. """
        # Check source types
        out_typearg = None
        fun_type = self.fun_type
        if fun_type.is_type_fun:
            # Since this is a type function, also check parameters
            for param in fun_type.type_params:
                if param == name:
                    return KindType
            
            # Did not match any type params
            fun_type = fun_type.type_expr.resolve()
            assert fun_type.is_function_type

        for typearg in fun_type.source_typeargs:
            if typearg.name == name:
                out_typearg = typearg
                if out_typearg.type_expr == KindType:
                    set_trace()
                    # TODO: *something?*
                return out_typearg.type_expr

        # Check if this is the "output" arg
        if fun_type.return_typearg and fun_type.return_typearg.name == name:
            return fun_type.return_typearg.type_expr

        # Check locals
        if self.is_temp_variable(name):
            # Check local variables
            return self.temp_var_type(name)

        return out_typearg

    def _resolve(self):
        """
        The main resolver method.  This should take care of the following:

            1. Ensure field paths are correct
            2. All exprs have their evaluated types set
        """
        new_fun_type = self.fun_type.resolve()
        resolved_expr = None if not self.expr else self.expr.resolve()
        if new_fun_type == self.fun_type and resolved_expr == self.expr:
            return self
        out = Fun(self.name, new_fun_type, resolved_expr, self.parent, self.annotations, self.docs)
        return out

    def _evaltype(self):
        return self.resolve().fun_type

    def __repr__(self):
        return "<%s(0x%x) %s>" % (self.__class__.__name__, id(self), self.fqn)

    def matches_input(self, input_typeexprs):
        """Tells if the input types can be accepted as argument for this transformer."""
        from typecube import unifier as tlunifier
        assert type(input_typeexprs) is list
        if len(input_typeexprs) != len(self.source_typeargs):
            return False
        return all(tlunifier.can_substitute(st.type_expr, it) for (st,it) in izip(self.source_typeargs, input_typeexprs))

    def matches_output(self, output_typeexpr):
        from typecube import unifier as tlunifier
        return tlunifier.can_substitute(output_typeexpr, self.dest_typearg.type_expr)

    def is_temp_variable(self, varname):
        return varname in self.temp_variables

    def temp_var_type(self, varname):
        return self.temp_variables[str(varname)]

    def register_temp_var(self, varname, vartype = None):
        assert type(varname) in (str, unicode)
        if varname in (x.name for x in self.fun_type.source_typeargs):
            raise TLException("Duplicate temporary variable '%s'.  Same as function arguments." % varname)
        elif self.fun_type.return_typearg and varname == self.fun_type.return_typearg.name:
            raise TLException("Duplicate temporary variable '%s'.  Same as function return argument name." % varname)
        elif self.is_temp_variable(varname) and self.temp_variables[varname] is not None:
            raise TLException("Duplicate temporary variable declared: '%s'" % varname)
        self.temp_variables[varname] = vartype

class FunApp(Expr):
    """ Super class of all applications """
    def __init__(self, func_expr, func_args = None):
        super(FunApp, self).__init__()
        self.func_expr = func_expr
        if func_args and type(func_args) is not list:
            func_args = [func_args]
        self.func_args = func_args
        self.func_expr.parent = self
        for arg in self.func_args: arg.parent = self

    def _equals(self, another):
        return self.func_expr.equals(another.func_expr) and \
                self.func_args.equals(another.func_args)

    def _evaltype(self):
        resolved = self.resolve()
        if issubclass(resolved.__class__, App):
            resolved.func_expr.evaltype()
        elif isinstance(resolved, Type):
            return resolved
        else:
            set_trace()
            assert False, "What now?"

    def resolve_function(self):
        function = self.func_expr.resolve()
        if not function:
            raise errors.TLException("Fun '%s' is undefined" % (self.func_expr))
        while type(function) is Type and type.is_alias:
            assert len(function.args) == 1, "Typeref cannot have more than one child argument"
            function = function.args[0].type_expr.resolve()

        if type(function) is not Fun:
            set_trace()
            raise errors.TLException("Fun '%s' is not a function" % (self.func_expr))
        return function

    def __repr__(self):
        return "<FunApp(0x%x) Expr = %s, Args = (%s)>" % (id(self), repr(self.func_expr), ", ".join(map(repr, self.func_args)))

    def _resolve(self):
        """
        Processes an exprs and resolves name bindings and creating new local vars 
        in the process if required.
        """
        # First resolve the expr to get the source function
        # Here we need to decide if the function needs to be "duplicated" for each different type
        # This is where type re-ification is important - both at buildtime and runtime
        function = self.resolve_function()
        arg_values = [arg.resolve() for arg in self.func_args]

        # Wont do currying for now
        if len(arg_values) != len(function.source_typeargs):
            raise errors.TLException("Fun '%s' takes %d arguments, but encountered %d.  Currying or var args NOT YET supported." %
                                            (function.name, len(function.source_typeargs), len(self.func_args)))

        # TODO - check arg types match
        if function != self.func_expr or any(x != y for x,y in zip(arg_values, self.func_args)):
            # Only return a new expr if any thing has changed
            return FunApp(function, arg_values)
        return self

class Type(Expr, Annotatable):
    def __init__(self, fqn, parent, annotations = None, docs = ""):
        """
        Creates a new type function.  Type functions are responsible for creating concrete type instances
        or other (curried) type functions.

        Params:
            fqn             FQN of the type.
            parent          A reference to the parent container entity of this type.
            annotations     Annotations applied to the type.
            docs            Documentation string for the type.
        """
        Annotatable.__init__(self, annotations = annotations, docs = docs)
        Expr.__init__(self, parent)

        # tag can indicate a further specialization of the type - eg "record", "enum" etc
        self.tag = None
        self.is_external = False
        self.fqn = fqn

    @property
    def is_literal_type(self):
        # Named basic types
        return False

    @property
    def is_product_type(self): return False

    @property
    def is_sum_type(self): return False

    @property
    def is_function_type(self): return False

    @property
    def is_type_app(self): return False

    @property
    def is_type_fun(self): return False

    @property
    def is_typeref(self): return False

    @property
    def is_alias_type(self): return False

    @property
    def name(self):
        return self.fqn.split(".")[-1]

    def __json__(self, **kwargs):
        out = {}
        if self.fqn:
            out["fqn"] = self.fqn
        if kwargs.get("include_docs", False) and self.docs:
            out["docs"] = self.docs
        return out

class LiteralType(Type):
    @property
    def is_literal_type(self): return True

    def clone(self, newparent):
        return LiteralType(self.fqn, newparent, self.annotations, self.docs)

class AliasType(Type):
    def __init__(self, fqn, target_type, parent, annotations = None, docs = ""):
        Type.__init__(self, fqn, parent, annotations, docs)
        self.target_type = target_type
        assert istype(self.target_type)

    def clone(self):
        return make_alias(self.fqn, self.target_type, self.parent, self.annotations, self.docs)

    @property
    def is_alias_type(self): return True

class ContainerType(Type):
    def __init__(self, fqn, typeargs, parent, annotations = None, docs = ""):
        Type.__init__(self, fqn, parent, annotations, docs)
        self.args = typeargs
        for arg in self.args:
            arg.parent = arg.type_expr.parent = self

    def _equals(self, another):
        return self.fqn == another.fqn and \
               self.parent == another.parent and \
               self.args.equals(another.args)

class ProductType(ContainerType):
    def __init__(self, tag, fqn, typeargs, parent, annotations = None, docs = ""):
        ContainerType.__init__(self, fqn, typeargs, parent, annotations, docs)
        self.tag = tag

    @property
    def is_product_type(self): return True

class SumType(ContainerType):
    def __init__(self, tag, fqn, typeargs, parent, annotations = None, docs = ""):
        ContainerType.__init__(self, fqn, typeargs, parent, annotations, docs)
        self.tag = tag

    @property
    def is_sum_type(self): return True

class FunType(Type):
    """ Represents function types. """
    def __init__(self, fqn, source_typeargs, return_typearg, parent, annotations = None, docs = ""):
        Type.__init__(self, fqn, parent, annotations, docs)
        self.return_typearg = return_typearg
        self.source_typeargs = source_typeargs
        for arg in self.source_typeargs:
            arg.parent = arg.type_expr.parent = self
        if self.return_typearg:
            self.return_typearg.parent = self.return_typearg.type_expr.parent = self

    @property
    def is_function_type(self): return True

class TypeRef(Type):
    @property
    def is_typeref(self): return True

    def clone(self, newparent):
        return make_ref(self.fqn, newparent, self.annotations, self.docs)

    def _resolve(self):
        return self.resolve_name(self.fqn)

class TypeFun(Type):
    def __init__(self, fqn, type_params, type_expr, parent, annotations = None, docs = ""):
        Type.__init__(self, fqn, parent, annotations = None, docs = "")
        assert not type_expr or istype(type_expr)
        self.type_params = type_params
        self.type_expr = type_expr
        self.is_external = type_expr is None
        # Ok to set parent since if the type expr is a ref only the reference's parent set
        # but the "real" underlying parent will have its type pointing to where ever it was
        # created
        if type_expr:
            self.type_expr.parent = self

    def apply(self, typeargs):
        assert self.type_expr is not None
        bindings = dict(zip(self.type_params, typeargs))
        return self._reduce_type_with_bindings(self.parent, self.type_expr, bindings)

    def _reduce_type_with_bindings(self, parent, type_expr, bindings):
        if type_expr.is_literal_type:
            return type_expr
        elif type_expr.is_typeref:
            if type_expr.fqn in bindings:
                return bindings[type_expr.fqn].clone(parent)
            return type_expr.clone(parent)
        elif type_expr.is_alias_type:
            assert False
        elif type_expr.is_product_type or type_expr.is_sum_type:
            maker = make_product_type if type_expr.is_product_type else make_sum_type
            typeargs = [TypeArg(ta.name, self._reduce_type_with_bindings(None, ta.type_expr, bindings),
                                ta.is_optional, ta.default_value, ta.annotations, ta.docs) for ta in type_expr.args]
            return maker(type_expr.tag, type_expr.fqn, typeargs, parent, type_expr.annotations, type_expr.docs)
        elif type_expr.is_type_app:
            new_typefun = self._reduce_type_with_bindings(None, type_expr.typefun_expr, bindings)
            new_typeargs = [self._reduce_type_with_bindings(None, arg, bindings) for arg in type_expr.typeapp_args]
            return make_type_app(new_typefun, new_typeargs, parent, type_expr.annotations, type_expr.docs)
        else:
            set_trace()
        pass

    @property
    def is_type_fun(self): return True

    def _resolve_name(self, name, condition = None):
        for param in self.type_params:
            if param == name:
                if condition is None or condition(arg.type_expr):
                    return KindType
                break
        return None

class TypeApp(Type):
    def __init__(self, typefun_expr, typeapp_args, parent, annotations = None, docs = ""):
        Type.__init__(self, None, parent, annotations = None, docs = "")
        if type(typefun_expr) in (str, unicode):
            typefun_expr = make_ref(typefun_expr)
        self.typefun_expr = typefun_expr
        self.typeapp_args = typeapp_args
        assert(all(istype(t) for t in typeapp_args)), "All type args in a TypeApp must be Type sub classes"
        self.typefun_expr.parent = self
        for arg in self.typeapp_args:
            arg.parent = self

    @property
    def is_type_app(self): return True

    def _resolve(self):
        """ Resolves a type application. This will apply the type arguments to the type function. """
        # First resolve the expr to get the source function
        # Here we need to decide if the function needs to be "duplicated" for each different type
        # This is where type re-ification is important - both at buildtime and runtime
        typefun = self.typefun_expr.resolve()
        typeargs = [arg.resolve() for arg in self.typeapp_args]
        if not typefun:
            raise errors.TLException("Fun '%s' is undefined" % self.args[0])
        if not typefun.is_type_fun:
            raise errors.TLException("Fun '%s' is not a function" % typefun)

        # Wont do currying for now
        if len(typeargs) != len(typefun.type_params):
            raise errors.TLException("TypeFun '%s' takes %d arguments, but encountered %d.  Currying or var args NOT YET supported." %
                                            (typefun.name, len(typefun.source_typeargs), len(self.typeapp_args)))

        # TODO - check arg types match
        if typefun.is_external:
            # Then typefun has no expression where we can do beta reductions so just
            # return a new typeapp with the arguments instead
            return self

        return typefun.apply(typeargs)

class TypeArg(Expr, Annotatable):
    """ A type argument is a child of a given type.  Akin to a member/field of a type.  """
    def __init__(self, name, type_expr, is_optional = False, default_value = None, annotations = None, docs = ""):
        Expr.__init__(self, None)
        Annotatable.__init__(self, annotations, docs)
        self.name = name
        self.type_expr = type_expr
        self.is_optional = is_optional
        self.default_value = default_value or None

    def _equals(self, another):
        return self.name == another.name and \
                self.is_optional == another.is_optional and \
                (self.default_value == another.default_value or self.default_value.equals(another.default_value)) and \
                self.type_expr.equals(another.type_expr)

    def __json__(self, **kwargs):
        out = {}
        if self.name:
            out["name"] = self.name
        return out

    def _evaltype(self):
        """ Type of a "Type" is a KindType!!! """
        resolved = self.resolve()
        return resolved.type_expr.resolve()

    def _resolve(self):
        out = self
        if self.type_expr is None:
            return self
        new_expr = self.type_expr.resolve()
        if new_expr != self.type_expr:
            out =  TypeArg(self.name, new_expr, self.is_optional, self.docs, annotations = self.annotations, docs = self.docs)
        return out

    def unwrap_with_field_path(self, full_field_path):
        starting_var, field_path = full_field_path.pop()
        curr_typearg = self
        curr_path = curr_field_name = starting_var
        yield curr_field_name, curr_path, curr_typearg
        while field_path.length > 0:
            next_field_name, tail_path = field_path.pop()
            next_path = curr_path + "/" + next_field_name
            next_typearg = curr_typearg.type_expr.resolve().args.withname(next_field_name)
            curr_field_name, curr_path, field_path = next_field_name, next_path, tail_path
            yield curr_field_name, curr_path, curr_typearg

def validate_typearg(arg):
    if isinstance(arg, TypeArg):
        return arg
    elif issubclass(arg.__class__, Expr):
        return TypeArg(None, arg)
    elif type(arg) in (str, unicode):
        return TypeArg(None, Var(arg))
    else:
        raise errors.TLException("Argument must be a TypeArg, Expr or a string. Found: '%s'" % type(arg))

class TypeArgList(object):
    """ A list of type args for a particular type container. """
    def __init__(self, typeargs):
        self._typeargs = []
        for typearg in typeargs or []:
            self.add(typearg)

    def equals(self, another):
        return len(self._typeargs) == len(self._typeargs) and all(x.equals(y) for x,y in izip(self._typeargs, another._typeargs))

    def __getitem__(self, slice):
        return self._typeargs.__getitem__(slice)

    def __iter__(self): return iter(self._typeargs)

    def __len__(self): return len(self._typeargs)

    def __repr__(self):
        return repr(self._typeargs)

    @property
    def count(self): return len(self._typeargs)

    def index_for(self, name):
        for i,arg in enumerate(self._typeargs):
            if arg.name == name:
                return i
        return -1

    def withname(self, name):
        return self.atindex(self.index_for(name))

    def atindex(self, index):
        return None if index < 0 else self._typeargs[index]

    def contains(self, name):
        return self.index_for(name) >= 0

    def add(self, arg):
        """
        Add an argument type.
        """
        arg = validate_typearg(arg)
        if arg.name:
            index = self.index_for(arg.name)
            if index >= 0:
                raise errors.TLException("Child type by the given name '%s' already exists" % arg.name)
        self._typeargs.append(arg)

def make_literal_type(fqn, parent = None, annotations = None, docs = ""):
    return LiteralType(fqn, parent, annotations, docs)

def make_product_type(tag, fqn, typeargs, parent = None, annotations = None, docs = ""):
    return ProductType(tag, fqn, typeargs, parent, annotations = None, docs = "")

def make_sum_type(tag, fqn, typeargs, parent = None, annotations = None, docs = ""):
    return SumType(tag, fqn, typeargs, parent, annotations = None, docs = "")

def make_fun_type(fqn, source_typeargs, return_typearg, parent = None, annotations = None, docs = ""):
    return FunType(fqn, source_typeargs, return_typearg, parent, annotations, docs)

def make_alias(fqn, target_type, parent = None, annotations = None, docs = ""):
    return AliasType(fqn, target_type, parent, annotations, docs)

def make_type_fun(fqn, type_params, expr, parent, annotations = None, docs = ""):
    return TypeFun(fqn, type_params, expr, parent, annotations = None, docs = "")

def make_ref(target_fqn, parent = None, annotations = None, docs = None):
    return TypeRef(target_fqn, parent, annotations = annotations, docs = docs)

def make_type_app(type_func_expr, typeargs, parent = None, annotations = None, docs = ""):
    return TypeApp(type_func_expr, typeargs, parent, annotations, docs)

def make_enum_type(fqn, symbols, parent = None, annotations = None, docs = None):
    typeargs = []
    for name,value,sym_annotations,sym_docs in symbols:
        typeargs.append(TypeArg(name, VoidType, False, value, sym_annotations, sym_docs))
    out = SumType("enum", fqn, typeargs, parent, annotations = annotations, docs = docs)
    for ta in typeargs:
        ta.type_expr = out
        # ta.type_expr.parent = out
    return out

KindType = make_literal_type("Type")
AnyType = make_literal_type("any")
VoidType = make_literal_type("void")
