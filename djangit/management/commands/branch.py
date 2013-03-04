"""Commands for handling git branches."""

from djangit.utils import sh, boolval
from _private import BranchCommand


class Command(BranchCommand):
    args = '<command> <branch>'
    help = 'Helper for creating and deleting branches,\
     including pushing/pulling origin and database copying.'

    def delete(self, branch_name, origin, with_db):
        """Delete the specified branch.

        args:
        branch_name -- name of branch to delete
        origin -- if True, delete the branch from the remote repository as well
        with_db -- if True, call drop_databases for the current branch name
        """
        sh('git branch -D %s' % branch_name)
        if origin:
            sh('git push origin :%s' % branch_name)
        if with_db:
            self.drop_databases(branch_name)

    def create(self, branch_name, origin, with_db):
        """Create a new branch.

        args:
        branch_name -- name of new branch
        origin -- if True, push new branch to remote repository
        with_db -- if True, call copy_databases for new branch
        """
        sh('git branch %s' % branch_name)
        if origin:
            sh('git push -u origin %s' % branch_name)
        if with_db:
            self.copy_databases(branch_name)

    def handle_branch(self, command, branch_name, **options):
        if command == 'create':
            self.create(branch_name, options['origin'], boolval(options['db']))
        elif command == 'delete':
            self.delete(branch_name, options['origin'], boolval(options['db']))
