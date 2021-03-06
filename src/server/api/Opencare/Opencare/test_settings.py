from project.local_settings import *
from django.test.runner import DiscoverRunner

class UnManagedModelTestRunner(DiscoverRunner):
    '''
    Test runner that automatically makes all unmanaged models in your Django
    project managed for the duration of the test run.
    Many thanks to the Caktus Group: http://bit.ly/1N8TcHW
    '''

    def setup_test_environment(self, *args, **kwargs):
        from django.db.models.loading import get_models
        self.unmanaged_models = [m for m in get_models() if not m._meta.managed]
        for m in self.unmanaged_models:
            m._meta.managed = True
        super(UnManagedModelTestRunner, self).setup_test_environment(*args, **kwargs)

    def teardown_test_environment(self, *args, **kwargs):
        super(UnManagedModelTestRunner, self).teardown_test_environment(*args, **kwargs)
        # reset unmanaged models
        for m in self.unmanaged_models:
            m._meta.managed = False

# Since we can't create a test db on the read-only host, and we
# want our test dbs created with postgres rather than the default, override
# some of the global db settings, only to be in effect when "test" is present
# in the command line arguments:

if 'test' in sys.argv or 'test_coverage' in sys.argv:  # Covers regular testing and django-coverage

    DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
    DATABASES['default']['HOST'] = '127.0.0.1'
    DATABASES['default']['USER'] = 'django'
    DATABASES['default']['PASSWORD'] = 'django'

    DATABASES['tmi']['ENGINE'] = 'django.db.backends.mysql'
    DATABASES['tmi']['HOST'] = '127.0.0.1'
    DATABASES['tmi']['USER'] = 'django'
    DATABASES['tmi']['PASSWORD'] = 'django'


# The custom routers we're using to route certain ORM queries
# to the remote host conflict with our overridden db settings.
# Set DATABASE_ROUTERS to an empty list to return to the defaults
# during the test run.

DATABASE_ROUTERS = []

# Set Django's test runner to the custom class defined above
TEST_RUNNER = 'project.test_settings.UnManagedModelTestRunner'
