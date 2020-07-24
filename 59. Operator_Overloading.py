# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:34:18 2019

@author: zakir
"""
class Phone:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price
    
    def full_name(self):
        return f"name: {self.name} \nmodel: {self.model} \nprice: {self.price}"
    
    def __add__(self,other):
        return (self.price + other.price)
    
    def __sub__(self,other):
        return (self.price - other.price)
    
    def __mul__(self,other):
        return (self.price * other.price)
    
    def __eq__(self,other):
        return (self.price == other.price)
    
    
    
p1=Phone("LG","G6",54000)
p2=Phone("Samsung","s10",110000)
print(p1+p2)
print(p2-p1)
print(p1==p2)


# =============================================================================
# __add__(	self, other)
# __sub__(	self, other)
# __mul__(	self, other)
# __floordiv__(	self, other)
# __mod__(	self, other)
# __divmod__(	self, other)
# __pow__(	self, other[, modulo])
# __lshift__(	self, other)
# __rshift__(	self, other)
# __and__(	self, other)
# __xor__(	self, other)
# __or__(	self, other)
# These methods are called to implement the binary arithmetic operations (+, -, *, //, %, divmod(), pow(), **, <<, >>, &, ^, |). For instance, to evaluate the expression x+y, where x is an instance of a class that has an __add__() method, x.__add__(y) is called. The __divmod__() method should be the equivalent to using __floordiv__() and __mod__(); it should not be related to __truediv__() (described below). Note that __pow__() should be defined to accept an optional third argument if the ternary version of the built-in pow() function is to be supported.
# __div__(	self, other)
# __truediv__(	self, other)
# The division operator (/) is implemented by these methods. The __truediv__() method is used when __future__.division is in effect, otherwise __div__() is used. If only one of these two methods is defined, the object will not support division in the alternate context; TypeError will be raised instead.
# __radd__(	self, other)
# __rsub__(	self, other)
# __rmul__(	self, other)
# __rdiv__(	self, other)
# __rtruediv__(	self, other)
# __rfloordiv__(	self, other)
# __rmod__(	self, other)
# __rdivmod__(	self, other)
# __rpow__(	self, other)
# __rlshift__(	self, other)
# __rrshift__(	self, other)
# __rand__(	self, other)
# __rxor__(	self, other)
# __ror__(	self, other)
# These methods are called to implement the binary arithmetic operations (+, -, *, /, %, divmod(), pow(), **, <<, >>, &, ^, |) with reflected (swapped) operands. These functions are only called if the left operand does not support the corresponding operation and the operands are of different types.3.2 For instance, to evaluate the expression x-y, where y is an instance of a class that has an __rsub__() method, y.__rsub__(x) is called if x.__sub__(y) returns NotImplemented.
# Note that ternary pow() will not try calling __rpow__() (the coercion rules would become too complicated).
# 
# Note: If the right operand's type is a subclass of the left operand's type and that subclass provides the reflected method for the operation, this method will be called before the left operand's non-reflected method. This behavior allows subclasses to override their ancestors' operations.
# 
# __iadd__(	self, other)
# __isub__(	self, other)
# __imul__(	self, other)
# __idiv__(	self, other)
# __itruediv__(	self, other)
# __ifloordiv__(	self, other)
# __imod__(	self, other)
# __ipow__(	self, other[, modulo])
# __ilshift__(	self, other)
# __irshift__(	self, other)
# __iand__(	self, other)
# __ixor__(	self, other)
# __ior__(	self, other)
# These methods are called to implement the augmented arithmetic operations (+=, -=, *=, /=, %=, **=, <<=, >>=, &=, ^=, |=). These methods should attempt to do the operation in-place (modifying self) and return the result (which could be, but does not have to be, self). If a specific method is not defined, the augmented operation falls back to the normal methods. For instance, to evaluate the expression x+=y, where x is an instance of a class that has an __iadd__() method, x.__iadd__(y) is called. If x is an instance of a class that does not define a __iadd__() method, x.__add__(y) and y.__radd__(x) are considered, as with the evaluation of x+y.
# __neg__(	self)
# __pos__(	self)
# __abs__(	self)
# __invert__(	self)
# Called to implement the unary arithmetic operations (-, +, abs() and ~).
# __complex__(	self)
# __int__(	self)
# __long__(	self)
# __float__(	self)
# Called to implement the built-in functions complex(), int(), long(), and float(). Should return a value of the appropriate type.
# __oct__(	self)
# __hex__(	self)
# Called to implement the built-in functions oct() and hex(). Should return a string value.
# __coerce__(	self, other)
# Called to implement ``mixed-mode'' numeric arithmetic. Should either return a 2-tuple containing self and other converted to a common numeric type, or None if conversion is impossible. When the common type would be the type of other, it is sufficient to return None, since the interpreter will also ask the other object to attempt a coercion (but sometimes, if the implementation of the other type cannot be changed, it is useful to do the conversion to the other type here). A return value of NotImplemented is equivalent to returning None.
# 
# =============================================================================
# =============================================================================

