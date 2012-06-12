#!/usr/bin/python

# found example here: http://www.velocityreviews.com/forums/t396797-dynamic-runtime-code-introspection-compilation.html

import sys

somecode = """
class Foo:
    param1 = "Hello, world!"
"""

plugin = type(sys)('unknown_plugin') # Create new empty module
exec somecode in plugin.__dict__

print plugin.Foo.param1

print dir(plugin.Foo)


