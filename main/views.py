from django.http import HttpResponse, JsonResponse
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "main\main.html")

@login_required
def save_value(request):
    if request.method == "POST":
        value = request.POST.get("value")
        
        return JsonResponse(data={"access": "access"})
    else:
        return HttpResponse(status=404)