class Engine(object):
    def __init__(self, db, branch_db_name):
        self.db = db
        self.branch_db_name = branch_db_name

    def _get_command(self, cmd_name):
        command = getattr(self.__class__, cmd_name)
        return command.format(
            BRANCH_DB=self.branch_db_name,
            **self.db)

    def get_copy_command(self):
        return self._get_command('copy_command')

    def get_drop_command(self):
        return self._get_command('drop_command')
