from optparse import make_option
import operator

from django.core.management.base import BaseCommand, CommandError
from django.utils import translation

from djangit.db import get_engine
from djangit.utils import sh, db_name


class BranchCommand(BaseCommand):
    can_import_settings = True
    option_list = BaseCommand.option_list + (
        make_option('--origin',
            action='store_true',
            dest='origin',
            default=False,
            help='Include changes in origin.'),
        make_option('--db',
            action='store',
            dest='db',
            default=True,
            help='Include changes to database.'),
    )

    def _perform_branch_db_operation(self, branch_name, method_name):
        for db in self.databases.values():
            engine = get_engine(db, db_name(db['NAME'], branch_name))
            sh(operator.methodcaller(method_name)(engine))

    def copy_databases(self, branch_name):
        return self._perform_branch_db_operation(branch_name, 'get_copy_command')

    def drop_databases(self, branch_name):
        return self._perform_branch_db_operation(branch_name, 'get_drop_command')

    def handle_branch(self, *args, **options):
        """Implement this for custom commands in subclasses."""
        pass

    def handle(self, *args, **options):
        from django.conf import settings
        try:
            self.databases = settings.DATABASES_ORIGINAL
        except AttributeError:
            self.databases = settings.DATABASES
        translation.activate(settings.LANGUAGE_CODE)

        self.handle_branch(*args, **options)

        translation.deactivate()
