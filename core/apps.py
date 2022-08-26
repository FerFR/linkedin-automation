from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from core.jobs import post_in_linkedin, clear_photos
        scheduler = BackgroundScheduler()
        scheduler.add_job(post_in_linkedin,'interval',minutes=1)
        scheduler.add_job(clear_photos,'interval',minutes=1)
        scheduler.start()