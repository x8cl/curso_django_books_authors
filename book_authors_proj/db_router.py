from django.conf import settings
 
DATABASE_MAPPING = settings.DATABASE_APPS_MAPPING
 
class DatabaseAppsRouter(object):
    def db_for_read(self, model, **hints):
        """ Dirija todas las operaciones de lectura a una base de datos específica. """
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        """ Dirija todas las operaciones de escritura a una base de datos específica. """
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """ Permitir cualquier relación entre aplicaciones que utilicen la misma base de datos """
        db_obj1 = DATABASE_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        else:
            return None
    
    def allow_syncdb(self, db, model):
        """ Asegúrese de que estas aplicaciones solo aparezcan en la base de datos correspondiente. """
        if db in DATABASE_MAPPING.values():
            return DATABASE_MAPPING.get(model._meta.app_label) == db
        elif model._meta.app_label in DATABASE_MAPPING:
            return False
        return None
    
    def allow_migrate(self, db, app_label, model=None, **hints):
        """ Asegúrese de que la aplicación de autenticación solo aparezca en la base de datos" authdb ". """
        if db in DATABASE_MAPPING.values():
            return DATABASE_MAPPING.get(app_label) == db
        elif app_label in DATABASE_MAPPING:
            return False
        return None