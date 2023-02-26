import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

import django
django.setup()

from django.core.management import call_command

import csv
from core.models import Account


try:
    with open('user-list.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            client_id = row.get('client_id')
            email = row.get('preferences.trendyolAccountId')
            password = row.get('preferences.trendyolAccountPwd')
            if client_id != '' and '@' in email and password != '':
                print(client_id, email, password)
                Account.objects.get_or_create(client_id=client_id, email=email, password=password)
except Exception as e:
    print(e)
