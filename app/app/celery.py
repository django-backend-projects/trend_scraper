from __future__ import absolute_import
from __future__ import unicode_literals

import logging
import os
from django.conf import settings
from celery import Celery

from celery.schedules import crontab



logger = logging.getLogger("Celery")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

app = Celery("app")

app.config_from_object("django.conf:settings", namespace="CELERY")


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks()



@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))


app.conf.beat_schedule = {
    'rerun_fail_dec': {
        'task': 'core.tasks.rerun_fail_dec',
        'schedule': crontab(hour=10, minute=0),
    },
}


# if settings.PROD:
#     app.conf.update(
#         BROKER_URL='redis://:{password}@redis:6379/0'.format
#         (password='dKqs72RhtaPPYyfN'
#          ),
#         # CELERYBEAT_SCHEDULER='django_celery_beat.schedulers:DatabaseScheduler',
#         CELERY_RESULT_BACKEND='redis://:{password}@redis:6379/1'.format(
#             password='dKqs72RhtaPPYyfN'
#         ),
#         CELERY_DISABLE_RATE_LIMITS=True,
#         CELERY_ACCEPT_CONTENT=['json', ],
#         CELERY_TASK_SERIALIZER='json',
#         CELERY_RESULT_SERIALIZER='json',
#     )
# else:
#     app.conf.update(
#         BROKER_URL='redis://localhost:6379/0',
#         # CELERYBEAT_SCHEDULER='django_celery_beat.schedulers:DatabaseScheduler',
#         CELERY_RESULT_BACKEND='redis://localhost:6379/1',
#         CELERY_DISABLE_RATE_LIMITS=True,
#         CELERY_ACCEPT_CONTENT=['json', ],
#         CELERY_TASK_SERIALIZER='json',
#         CELERY_RESULT_SERIALIZER='json',
#     )

# if settings.PROD:
#     app.conf.update(
#         BROKER_URL='redis://:dKqs72RhtaPPYyfN@redis:6379/0',
#         CELERYBEAT_SCHEDULER='django_celery_beat.schedulers:DatabaseScheduler',
#         CELERY_RESULT_BACKEND='redis://:dKqs72RhtaPPYyfN@redis:6379/1',
#         CELERY_DISABLE_RATE_LIMITS=True,
#         CELERY_ACCEPT_CONTENT=['json', ],
#         CELERY_TASK_SERIALIZER='json',
#         CELERY_RESULT_SERIALIZER='json',
#     )
# else:
#     app.conf.update(
#         BROKER_URL='redis://localhost:6379/0',
#         CELERYBEAT_SCHEDULER='django_celery_beat.schedulers:DatabaseScheduler',
#         CELERY_RESULT_BACKEND='redis://localhost:6379/1',
#         CELERY_DISABLE_RATE_LIMITS=True,
#         CELERY_ACCEPT_CONTENT=['json', ],
#         CELERY_TASK_SERIALIZER='json',
#         CELERY_RESULT_SERIALIZER='json',
#     )
