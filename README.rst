pynames
*******

Count and present the usage of names in python source code.

Install
=======

Install from github::

  > pip3 install git+git://github.com/hevi9/pynames.git

Requirements::

  * Python 3
  * jinja2

Usage
=====

List name usage to terminal, for example in this pynames project::

  > pynames pynames/*.py
  
==>::

  1 *
  5 ARGS
  3 AST
  1 ArgumentParser
  1 D
  1 DEBUG
  ..
  
List name usage to html file, for example in this pynames project::

  > pynames --html out.html pynames/*.py
  > firefox out.html
  
==> out.html
  
  