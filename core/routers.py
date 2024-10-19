from django.conf import settings
from apps.dashboard.models import ParsedSessions, TestSessionSchools, OLDAuthUser

class OldDBRouter:
    """
    A router to control all database operations on models in the
    ParsedSessions, TestSessionSchools, and OLDAuthUser.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read ParsedSessions, TestSessionSchools, and OLDAuthUser models go to old_db.
        """
        if model in [ParsedSessions, TestSessionSchools, OLDAuthUser]:
            return 'old_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write ParsedSessions, TestSessionSchools, and OLDAuthUser models go to old_db.
        """
        if model in [ParsedSessions, TestSessionSchools, OLDAuthUser]:
            return 'old_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the ParsedSessions, TestSessionSchools, or OLDAuthUser is involved.
        """
        if obj1._meta.model in [ParsedSessions, TestSessionSchools, OLDAuthUser] or \
           obj2._meta.model in [ParsedSessions, TestSessionSchools, OLDAuthUser]:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the ParsedSessions, TestSessionSchools, and OLDAuthUser models only appear in the 'old_db'
        database.
        """
        if model_name in ['parsedsessions', 'testsessionschools', 'oldauthuser']:
            return db == 'old_db'
        return None