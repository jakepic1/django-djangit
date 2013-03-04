from importlib import import_module

engine_modules = {
    'mysql': 'mysql',
}

def get_engine(db, branch_db_name):
    backend = db['ENGINE'].split('.')[-1]

    try:
        module_name = engine_modules[backend]
    except KeyError:
        raise ValueError('Database backend %s not implemented.' % backend)

    module = import_module('djangit.db.%s' % module_name)
    return module.Engine(db, branch_db_name)
