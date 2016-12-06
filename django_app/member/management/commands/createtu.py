import json
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
User = get_user_model()
CONF_DIR = settings.CONF_DIR
config = json.loads(open(os.path.join(CONF_DIR, 'settings_deploy.json')).read())


class Command(BaseCommand):
    def handle(self, *args, **options):
        testUsers = config['testUsers']

        for testUser in testUsers:
#            print( testUser['username'], testUser['password'], testUser['email'] )

            username = testUser['username']
            password = testUser['password']
            email = testUser['email']

            if not User.objects.filter(username=username).exists():
                User.objects.create_user(
                    username=username,
                    password=password,
                    email=email)
                print('testUser[{}] created'.format(username))

