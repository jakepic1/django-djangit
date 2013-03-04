import copy
import subprocess

from djangit.utils import sh, db_name


def setup_dbs(databases, branches_to_ignore=None):
    curr_branch = sh('git rev-parse --abbrev-ref HEAD', False)

    if branches_to_ignore is None:
        branches_to_ignore = ()

    if curr_branch not in branches_to_ignore:
        for db in databases.values():
            db['NAME'] = db_name(db['NAME'], curr_branch)

def copy_original_dbs(databases):
    return copy.deepcopy(databases)
