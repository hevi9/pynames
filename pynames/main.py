#!/usr/bin/env python3
## -*- coding: utf-8 -*-
## Copyright (C) 2014 Petri Heinilä, LGPL 2.1

import sys      # http://docs.python.org/py3k/library/sys.html
import argparse # http://docs.python.org/py3k/library/argparse.html
import logging  # http://docs.python.org/py3k/library/logging.html
import datetime
log = logging.getLogger(__name__)
D = log.debug
I = log.info
E = log.error
from pynames.ast_visit import Visitor
from pynames.stats import Stats
import ast
import jinja2

##############################################################################

def extract(file, stats):
  with open(file) as fo:
    code = fo.read()
  tree = ast.parse(code, file)
  v = Visitor(stats.add_name, file)
  v.visit(tree)

def report(stats):
  print("\n".join(["%s\t%s" % (stats.names[x].count,x) for x in sorted(stats.names)]))

def report_html(stats, html_file):
  jenv = jinja2.Environment(loader=jinja2.PackageLoader("pynames", "default"))
  tmpl = jenv.get_template("file.html")
  ctx = {
    "page": {
       "title": "pynames",
       "time": datetime.datetime.now().isoformat(),
     },
    "stats": stats
  }
  log.info("generating %s", html_file)
  with open(html_file,"w") as fd:
    fd.write(tmpl.render(ctx))

##############################################################################

ARGS = argparse.ArgumentParser()
ARGS.add_argument("files", 
                  metavar="file.py",
                  nargs="+",
                  help="python files to lookup names")
ARGS.add_argument("-d", "--debug", 
                  action="store_true",
                  help="set debugging on")
ARGS.add_argument("--html",
                  metavar="FILE",
                  help="produce html file")

def main():
  args = ARGS.parse_args()
  logging.basicConfig()
  if args.debug:
    logging.getLogger().setLevel(logging.DEBUG)
  stats = Stats()
  for file in args.files:
    extract(file, stats)
  if args.html:
    report_html(stats, args.html)
  else:
    report(stats)
  sys.exit(0)


if __name__ == "__main__":
  main()
  
