from django.http import HttpResponse, JsonResponse
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db import transaction

from user.models import User

# Create your views here.
def index(request):

    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
    else: user = None

    context = {
        "user": user,
    }

    return render(request, "main\main.html", context=context)


@login_required
def save_value(request):
    if request.method == "POST":
        value = request.POST.get("value")
        key = f"value_{request.user.pk}"
        cache.set(key=key, value=value, timeout=3600)
        # print(f"Score: {cache.get(key=key)} for: {request.user.username}")
        
        return JsonResponse(data={"access": True})
    else:
        return HttpResponse(status=404)


@login_required
def delete_data_from_cache(request):
    if request.method == "POST":
        user = request.user
        key = f"value_{user.pk}"
        if cache.get(key=key):
            try:
                with transaction.atomic():
                    user.score = cache.get(key=key)
                    user.save()
                    cache.delete(key=key)
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)
            
            data = {"value": user.score}
            return JsonResponse(data)
        else:
            return JsonResponse({"error": "No data found in cache"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)