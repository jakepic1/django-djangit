"""Utilities to be used in django's settings.py."""

import copy
import subprocess

from djangit.utils import sh, db_name


def setup_dbs(databases, branches_to_ignore=None):
    """Append the current branch name to NAME values of all databases.

    args:
    databases -- django settings DATABASES
    branches_to_ignore -- if the current branch is in branches_to_ignore, the names of databases will not be changed. (default None)
    """
    curr_branch = sh('git rev-parse --abbrev-ref HEAD', False)

    if branches_to_ignore is None:
        branches_to_ignore = ()

    if curr_branch not in branches_to_ignore:
        for db in databases.values():
            db['NAME'] = db_name(db['NAME'], curr_branch)

def copy_original_dbs(databases):
    """Return a deep copy of the original databases."""
    return copy.deepcopy(databases)
