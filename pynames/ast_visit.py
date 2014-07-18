#!/usr/bin/env python3
## -*- coding: utf-8 -*-
## Copyright (C) 2014 Petri Heinilä, LGPL 2.1

import ast
from pprint import pprint
#from astpp import dump
import logging
log = logging.getLogger(__name__)

# Do not report these AST nodes as not handled. There might be smarter 
# implementation, but I liked to see what code has been eaten.
SKIP = [
  "Add",
  "Num",
  "BinOp",
  "Pass",
  "Module",
  "Assign",
  "Store",
  "Expr",
  "arguments",
  "Load",
  "Call",
  "Str",
  "If",
  "withitem",
  "With",
  "keyword",
  "comprehension",
  "Index",
  "Subscript",
  "Tuple",
  "Mod",
  "ListComp",
  "NotIn",
  "Compare",
  "List",
  "Import",
  "Return",
  "In",
  "Del",
  "Eq",
  "Or",
  "Is",
  "Not",
  "IsNot",
  "And",
  "USub",
  "UnaryOp",
  "NotEq",
  "Try",
  "Raise",
  "Delete",
  "Bytes",
  "While",
  "Dict",
  "For",
  "Continue",
  "Slice",
  "BoolOp",
  "LShift",
  "Yield",
  "YieldFrom",
  "Break",
  "Set",
  "LtE",
  "GeneratorExp",
  "NameConstant",
  "Lambda",
  "Lt",
  "Gt",
  "Sub",
  "GtE",
  "Mult",
  "Invert",
  "BitAnd",
  "FloorDiv",
  "Pow",
  "Div",
  "Assert",
  "BitXor",
  "BitOr",
  "IfExp",
  "RShift",
  "AugAssign",
  "UAdd",
  "Ellipsis",
  "DictComp",
  "Starred",
  "SetComp"
]

class Visitor(ast.NodeVisitor):

  def __init__(self, add_name_cb, file):
    self._add_name_cb = add_name_cb
    self._file = file
  
  def generic_visit(self, node):
    not_handled(node)
    super().generic_visit(node)

  def visit_arg(self, node):
    if node.arg is not None:
      self._add_name_cb(node.arg)
    if node.annotation:
      not_handled(node.annotation)
    super().generic_visit(node)

  def visit_alias(self, node):
    if node.name is not None:
      self._add_name_cb(node.name)
    super().generic_visit(node)
    
  def visit_ImportFrom(self, node):
    if node.module is not None:
      self._add_name_cb(node.module)
    super().generic_visit(node)
    
  def visit_Name(self, node):
    if node.id is not None:
      self._add_name_cb(node.id)
    super().generic_visit(node)
    
  def visit_ClassDef(self, node):
    if node.name is not None:
      self._add_name_cb(node.name)
    super().generic_visit(node)

  def visit_FunctionDef(self, node):
    if node.name is not None:
      self._add_name_cb(node.name)
    super().generic_visit(node)

  def visit_Attribute(self, node):
    if node.attr is not None:
      self._add_name_cb(node.attr)
    super().generic_visit(node)

  def visit_ExceptHandler(self, node):
    if node.name is not None:
      self._add_name_cb(node.name)
    super().generic_visit(node)

  def visit_Global(self, node):
    if node.names is not None:
      for name in node.names:
        self._add_name_cb(name)
    super().generic_visit(node)

  def visit_Nonlocal(self, node):
    if node.names is not None:
      for name in node.names:
        self._add_name_cb(name)
    super().generic_visit(node)
    


def not_handled(obj):
  if isinstance(obj, ast.AST):
    name = obj.__class__.__name__
    if name not in SKIP:
      fields = list()
      for field in obj._fields:
        fields.append("%s=%s" % (field,getattr(obj, field)))
      log.warn("not handled %s %s", name , ",".join(fields))
  else:
    log.warn("not handled %s", obj)



