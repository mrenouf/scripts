#!/usr/bin/python

import sys;
import os;
import re;
from sets import Set

def main(argv=None):
  if argv is None:
        argv = sys.argv
  path = argv[1];
    
  p = re.compile(r"(.*)\.(png|jpg|jpeg|gif)$", re.I)
  r = re.compile(r"[-_\(\)#\$\*\&%@!^]");
  cc = re.compile(r"(\s+)([a-z]\S*)");

  # Java reserved keywords:
  # http://java.sun.com/docs/books/tutorial/java/nutsandbolts/_keywords.html
  reserved = Set(['abstract', 'assert', 'boolean', 'break', 
    'byte', 'case', 'catch', 'char', 'class', 'const', 'continue', 
    'default', 'do', 'double', 'else', 'enum', 'extends', 'final',
    'finally', 'float', 'for', 'goto', 'if', 'implements', 'import', 
    'instanceof', 'int', 'interface', 'long', 'native', 'new', 
    'package', 'private', 'protected', 'public', 'return', 'short', 
    'static', 'strictfp', 'super', 'switch', 'synchronized', 'this', 
    'throw', 'throws', 'transient', 'try', 'void', 'volatile', 'while'])
        
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
        if name in reserved:
            name += "_";
        print "  @Resource(\"%s\")" % entry
        print "  public AbstractImagePrototype %s();" % name
        print
  print "}"
  return 0;

if __name__ == "__main__":
  sys.exit(main())

 
