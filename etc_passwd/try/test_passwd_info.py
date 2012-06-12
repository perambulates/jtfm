#!/usr/bin/python

import os, sys
import re
import types

module_skip_re = re.compile(r'^__')
# 
# following based on
# http://code.activestate.com/recipes/436873-import-modulesdiscover-methods-from-a-directory-na/
def import_modules(dir="./transform"):
    module_list = []
    for f in os.listdir(os.path.abspath(dir)):
        module_name, ext = os.path.splitext(f)
        if ext != '.py' or module_skip_re.match(module_name):
            continue
        print 'importing module: %s' % (module_name)
        #works:
        #module = __import__('transform.' + module_name,fromlist=[module_name],level=-1)
        #works, but pollutes our namespace instead of making accessible under
        #"transform."
        module_list.append(__import__('transform.' + module_name))

    return module_list


transforms = import_modules('./transform')
#print dir()

skip_specials = re.compile(r'^__(\w+)__$')

data=''
with open('/etc/passwd', 'r') as p:
    data = p.read()


for t in transforms:
    print "--- %s ---" % t.__name__
    print dir(t)

    for symbol in dir(t):
        print "checking symbol name %s" % symbol
        if skip_specials.match(symbol):
            continue
        m = getattr(t, symbol)
        if not type(m) == types.ModuleType:
            continue
        print "%s is a module" % symbol
        for mod_symbol in dir(m):
            print "checking symbol name %s in module %s" %(mod_symbol, m)
            a = getattr(m, mod_symbol)
            if not type(a) == types.FunctionType:
                continue
            print "%s is a function" % mod_symbol
            if mod_symbol == 'transform':
                print "transform doc"
                print a.__doc__


        

