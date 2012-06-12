#!/usr/bin/python

import re
lines_re=re.compile(r'[\n]+')
cols_re=re.compile(r':')

lookup = {
    'etc_passwd_shell_column': 6,
    'os_type': 'linux'
}

def skip():
    os_type = get_key('os_type')
    return os_type not in ('linux', 'unix')

def get_key(key):
    return lookup[key]


def handle_data(data):
    """
    look through our input to identify users with no shell or shell
    that is /bin/false
    """
    col = get_key("etc_passwd_shell_column")

    all_users = (cols_re.split(l.rstrip())[0:col+1:col] for l in lines_re.split(data.rstrip()))
    print repr(all_users)
    sans_shell = [u[0] for u in all_users if not u[1] or u[1] == '/bin/false']
    #return {'users_with_no_homes': [filter(lambda u: not u[1], all_users)] }
    return {'users_with_no_shell': sans_shell}


data=''
with open('/etc/passwd', 'r') as p:
    data=p.read()

results = handle_data(data)

print "results:"
print repr(results)

