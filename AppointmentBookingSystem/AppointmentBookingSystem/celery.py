from datetime import timezone
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppointmentBookingSystem.settings')

app = Celery('project_celery')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')

# celery beat settings
app.conf.beat_schedule = {

}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

