"""Helpful utility functions."""

import subprocess

def sh(command, print_output=True):
    """Run and return output from the specified command in the shell.

    optional args:
    print_output -- if True, print output from the shell (default True)
    """
    result = subprocess.check_output(command, shell=True).strip()
    if print_output:
        print command
        if result:
            print '\t%s' % result
    return result

def boolval(val):
    """Return a parsed string as either True or False."""
    if isinstance(val, bool):
        return val

    if val.lower() in ('0', 'false',):
        return False
    elif val.lower() in ('1', 'true',):
        return True
    raise TypeError('Cannot parse %s to bool.' % val)

def db_name(old_db_name, branch_name):
    """Concatenate the old database name with the new branch name."""
    return '%s_%s' % (old_db_name, branch_name)
