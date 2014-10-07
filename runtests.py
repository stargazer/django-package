import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'testproject.settings'
test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)

# Necessary for Django 1.7. See https://docs.djangoproject.com/en/dev/releases/1.7/#app-loading-changes
import django
if django.get_version().startswith('1.7'):
    django.setup()

from django.test.utils import get_runner
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

def run():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True, failfast=True)
    failures = test_runner.run_tests(['testproject',])
    sys.exit(failures)
