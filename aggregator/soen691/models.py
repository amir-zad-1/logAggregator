from django.db import models


class Log(models.Model):
    time_local = models.CharField(max_length=200)
    remote_addr = models.CharField(max_length=200)
    request = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    req_time = models.CharField(max_length=50)
    http_user_agent = models.CharField(max_length=500)
