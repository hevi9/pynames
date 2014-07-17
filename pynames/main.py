#!/usr/bin/env python3
## -*- coding: utf-8 -*-
## Copyright (C) 2014 Petri Heinilä, LGPL 2.1

import sys      # http://docs.python.org/py3k/library/sys.html
import argparse # http://docs.python.org/py3k/library/argparse.html
import logging  # http://docs.python.org/py3k/library/logging.html
log = logging.getLogger(__name__)
D = log.debug
I = log.info
E = log.error
from pynames.ast_visit import Visitor
from pynames.stats import Stats
import ast

##############################################################################

def extract(file, stats):
  with open(file) as fo:
    code = fo.read()
  tree = ast.parse(code)
  v = Visitor(stats.add_name, file)
  v.visit(tree)


##############################################################################

ARGS = argparse.ArgumentParser()
ARGS.add_argument("files", nargs="*",
                  help="Python files to lookup names")
ARGS.add_argument("-d", "--debug", action="store_true",
                  help="set debugging on")

def main():
  args = ARGS.parse_args()
  logging.basicConfig()
  if args.debug:
    logging.getLogger().setLevel(logging.DEBUG)
  stats = Stats()
  for file in args.files:
    extract(file, stats)
  stats.report()
  sys.exit(0)


if __name__ == "__main__":
  main()
  