#!/usr/bin/env python3
## -*- coding: utf-8 -*-
## Copyright (C) 2014 Petri Heinilä, LGPL 2.1

import logging
log = logging.getLogger(__name__)

class Item:
  
  def __init__(self, name):
    self.name = name
    self.count = 0

class Stats:

  def __init__(self):
    self.names = dict() # name: Item

  def add_name(self, name):
    #log.info("name=%s", name)
    assert name is not None
    if name in self.names:
      item = self.names[name]
    else:
      item = Item(name)
      self.names[name] = item
    item.count += 1


