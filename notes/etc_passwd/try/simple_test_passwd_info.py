#!/usr/bin/python

# TODO: dynamically generate the list of transforms
import transform.passwd_info

print dir(transform.passwd_info)

data=''
with open('/etc/passwd', 'r') as p:
    data = p.read()


