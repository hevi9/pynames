import logging
log = logging.getLogger(__name__)

class Stats:

  def __init__(self):
    self.names = dict()

  def add_name(self, name):
    #log.info("name=%s", name)
    assert name is not None
    self.names[name] = self.names.setdefault(name, 0) + 1

  def report(self):
    print("\n".join(["%s\t%s" % (self.names[x],x) for x in sorted(self.names)]))

