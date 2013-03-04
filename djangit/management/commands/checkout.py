from djangit.utils import sh, boolval
from _private import BranchCommand


class Command(BranchCommand):
    args = '<branch>'
    help = 'Helper for git checkout,\
     including pulling from origin and database copying.'

    def checkout(self, branch_name, origin, with_db):
        if origin:
            sh('git fetch')
            sh('git checkout --track -b {b} origin/{b}'.format(b=branch_name))
            if with_db:
                self.copy_databases(branch_name)
        else:
            sh('git checkout %s' % branch_name)

    def handle_branch(self, branch_name, **options):
        self.checkout(branch_name, options['origin'], boolval(options['db']))
