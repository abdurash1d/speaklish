from django.conf import settings
from apps.dashboard.models import ParsedSessions, TestSessionSchools, OLDAuthUser, SchoolProfiles

class OldDBRouter:
    """
    A router to control all database operations on models in the
    ParsedSessions, TestSessionSchools, OLDAuthUser, and SchoolProfiles.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read ParsedSessions, TestSessionSchools, OLDAuthUser, and SchoolProfiles models go to old_db.
        """
        if model in [ParsedSessions, TestSessionSchools, OLDAuthUser, SchoolProfiles]:
            return 'old_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write ParsedSessions, TestSessionSchools, OLDAuthUser, and SchoolProfiles models go to old_db.
        """
        if model in [ParsedSessions, TestSessionSchools, OLDAuthUser, SchoolProfiles]:
            return 'old_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the ParsedSessions, TestSessionSchools, OLDAuthUser, or SchoolProfiles is involved.
        """
        if obj1._meta.model in [ParsedSessions, TestSessionSchools, OLDAuthUser, SchoolProfiles] or \
           obj2._meta.model in [ParsedSessions, TestSessionSchools, OLDAuthUser, SchoolProfiles]:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the ParsedSessions, TestSessionSchools, OLDAuthUser, and SchoolProfiles models only appear in the 'old_db'
        database.
        """
        if model_name in ['parsedsessions', 'testsessionschools', 'oldauthuser', 'schoolprofiles']:
            return db == 'old_db'
        return None