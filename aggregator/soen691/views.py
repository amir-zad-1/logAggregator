from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from soen691 import models
from django.views.decorators.csrf import csrf_exempt
import json


def index(req):
    logs = models.Log.objects.all()
    return render(req, 'dashboard.html', {"logs": logs})


@require_http_methods(["GET", "POST"])
@csrf_exempt
def insert_log(req):

    json_data = json.loads(req.body.decode('utf-8'))

    log = models.Log()
    log.time_local = json_data["time_local"]
    log.remote_addr = json_data["remote_addr"]
    log.request = json_data["request"]
    log.status = json_data["status"]
    log.req_time = json_data["request_time"]
    log.http_user_agent = json_data["http_user_agent"]
    log.save()

    return HttpResponse("ok")
