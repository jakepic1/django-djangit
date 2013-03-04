from djangit.utils import sh, boolval
from _private import BranchCommand


class Command(BranchCommand):
    args = '<command> <branch>'
    help = 'Helper for creating and deleting branches,\
     including pushing/pulling origin and database copying.'

    def delete(self, branch_name, origin, with_db):
        sh('git branch -D %s' % branch_name)
        if origin:
            sh('git push origin :%s' % branch_name)
        if with_db:
            self.drop_databases(branch_name)

    def create(self, branch_name, origin, with_db):
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
