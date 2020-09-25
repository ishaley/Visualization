from django.shortcuts import render
from . import models


def index(request):
    v1 = models.UserLoanOrder.objects.first()
    return render(request, 'index.html', {'v1': v1})