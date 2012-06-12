import re

required_keys = ['etc_passwd_shell_column', 'os_type']
provided_keys = ['users_with_no_shell']

lines_re=re.compile(r'[\n]+')
cols_re=re.compile(r':')

def transform(data):
    """
    look through our input to identify users with no shell or shell
    that is /bin/false

    outputs a dictionary like the following:
    { 'users_with_no_shell': ['syslog', 'messagebus', ...] }
    """
    col = get_key("etc_passwd_shell_column")
    all_users = (cols_re.split(l.rstrip())[0:col+1:col] for l in lines_re.split(data.rstrip()))
    sans_shell = [u[0] for u in all_users if not u[1] or u[1] == '/bin/false']
    return {'users_with_no_shell': sans_shell}


