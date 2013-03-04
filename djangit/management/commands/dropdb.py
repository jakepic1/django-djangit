"""Drop the databases for a given branch."""

from django.core.management.base import BaseCommand

from _private import BranchCommand

class Command(BranchCommand):
    option_list = BaseCommand.option_list

    def handle_branch(self, branch_name, **options):
        self.drop_databases(branch_name)
