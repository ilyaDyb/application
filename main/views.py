from django.http import HttpResponse, JsonResponse
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db import transaction

from decimal import Decimal

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
    
    
def leaderboard(request):
    users = User.objects.filter(score__gt=1).order_by("-score")
    context = {
        "users": users,
    }
    return render(request, "main/leaderboard.html", context=context)


@login_required()
def trade_score(request):
    user = request.user
    if user.end_game == True:
        return render(request, "main/trade_score.html")
    else:
        return HttpResponse(status=404)
    

@login_required()
def convert_score(request):
    if request.method == "POST":
        user = request.user
        score = request.POST.get("score")
        dollars = request.POST.get("dollars")
        if len(score) >= 6:
            if user.score >= int(score):
                user.score = user.score - int(score)
                user.balance += Decimal(dollars)
                user.save()

                return JsonResponse({"status": "Success", "response": f"You got {dollars}$"})
            else:
                return JsonResponse({"status": "You have not enough points"})
        else:
            return JsonResponse({"status": "Too few points to convert, minimum points: 100 000"})
    else:
        return HttpResponse(status=404)