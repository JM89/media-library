from datetime import datetime

from django.shortcuts import render


def index(request):
    return render(request, "website/index.html", {"message": "Helloworld displayed at " + str(datetime.now())})
