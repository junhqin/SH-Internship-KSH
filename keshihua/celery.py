import os
from celery import Celery
from django.conf import settings
import django
# 设置celery环境变量和django-celery的工作目录
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CeleryTask.settings")
django.setup()
# 实例化celery
app = Celery("demo", broker="redis://localhost:6379/1")
# queue_names = app.connection().channel().queues().keys()

# app.connection().channel().queue_purge(queue_names)

# 加载celery配置
app.config_from_object("django.conf:settings")

# 如果项目当中有task.py, 那么celery使用app当中的task来生成任务
# app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)
# app.autodiscover_tasks()