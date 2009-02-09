#!/usr/bin/python

import sys;
import os;
import re;

def main(argv=None):
  if argv is None:
        argv = sys.argv
  path = argv[1];
    
  p = re.compile(r"(.*)\.(png|jpg|jpeg|gif)$", re.I)
  r = re.compile(r"[-_\(\)#\$\*\&%@!^]");
  cc = re.compile(r"(\s+)([a-z]\S*)");
  
  print "public interface MyImageBundle extends ImageBundle {"
  dirs = os.listdir(path);
  for entry in dirs:
    x = os.path.join(path, entry)
    if (os.path.isfile(x)):
      m = p.match(entry)
      if (m is not None):
        name = m.group(1)
        name = r.sub(" ", name)
        name = cc.sub(lambda m : m.group(2).title(), name)
        print "  @Resource(\"%s\")" % entry
        print "  public AbstractImagePrototype %s();" % name
        print
  print "}"
  return 0;

if __name__ == "__main__":
  sys.exit(main())

