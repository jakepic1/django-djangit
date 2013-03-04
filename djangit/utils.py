import subprocess

def sh(command, print_output=True):
    result = subprocess.check_output(command, shell=True).strip()
    if print_output:
        print command
        if result:
            print '\t%s' % result
    return result

def boolval(val):
    if isinstance(val, bool):
        return val

    if val.lower() in ('0', 'false',):
        return False
    elif val.lower() in ('1', 'true',):
        return True
    raise TypeError('Cannot parse %s to bool.' % val)

def db_name(old_db_name, branch_name):
    return '%s_%s' % (old_db_name, branch_name)
