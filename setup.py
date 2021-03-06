#!/usr/bin/env python3
## -*- coding: utf-8 -*-
## Copyright (C) 2014 Petri Heinilä, LGPL 2.1

from setuptools import setup, find_packages

info = dict()
with open("INFO") as f:
  exec(f.read(),info)

setup(
  name=info["name"],
  version=info["version"],
  description=info["title"],
  author=info["author"],
  url=info["url"],
  license = info["license"],
  install_requires = ["jinja2"],
  zip_safe=False, 
  packages = ["pynames"],
  package_data = {
    "pynames": [
      "default/*",
    ]
  },  
  entry_points={
    "console_scripts": [
      "pynames=pynames.main:main"
    ]
  }
)