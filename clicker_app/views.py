from django.http.response import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from clicker_app.forms import UserForm, ImageUpload
from django.contrib.auth import authenticate, default_app_config, logout, login  # noqa: F401
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from clicker_app.models import Achievement, Upgrade, Account, OwnsUpgrade  # noqa: F401
from django.views import View
import os


def index(request):

    upgrades_list = Upgrade.objects.order_by("cost")
    upgrade_table_dict = {}

    for item in upgrades_list:
        upgrade_table_dict[item] = [item.cost, 0]

    if request.user.is_authenticated:
        purchased_list = OwnsUpgrade.objects.filter(account=request.user.account)
    else:
        purchased_list = []

    for p in purchased_list:
        if p.upgrade in upgrade_table_dict.keys():
            upgrade_table_dict[p.upgrade][1] = p.quantity

    # TODO: remove list index for whole leaderboard  when scrolling is implememnted
    leaderboard_list = Account.objects.order_by("-lifetime_points")

    ranking_list = Account.objects.order_by("-lifetime_points")

    clicks_per_second = 0
    for item in purchased_list:
        if item.upgrade.auto_click:
            clicks_per_second += item.upgrade.effect*item.quantity

    upgraded_click = 1
    for item in purchased_list:
        if not item.upgrade.auto_click:
            upgraded_click += item.upgrade.effect*item.quantity

    context_dict = {
        "leaderboard": leaderboard_list,
        "upgrade_table": upgrade_table_dict,
        "purchased_list": purchased_list,
        "ranking_list": ranking_list,
        "cps": clicks_per_second,
        "upgraded_click": upgraded_click,
    }
    response = render(request, "clicker_app/index.html", context=context_dict)
    return response


def about(request):
    response = render(request, "clicker_app/about.html")
    return response


def tutorial(request):
    response = render(request, "clicker_app/tutorial.html")
    return response


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse("clicker_app:index"))
            else:
                return HttpResponse("Your account is disabled")
        else:
            print("Invalid login details, please try again")
            return HttpResponse("Invalid login details supplied")
    else:
        response = render(request, "clicker_app/login.html")
        return response


def signup(request):
    registered = False  # registration unsuccessful initially
    if request.method == "POST":  # if form is post, attempt to process
        user_form = UserForm(request.POST)  # take information from form
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            account = Account.objects.create(user=user)
            account.user = user
            account.save()

            for upgrade_instance in Upgrade.objects.all():
                owns_upgrade = OwnsUpgrade.objects.get_or_create(account=account, upgrade=upgrade_instance)[0]
                owns_upgrade.save()

            registered = True  # save to databbase, registration successful
        else:
            print(user_form.errors)  # invalid attempt
    else:
        user_form = UserForm()  # give blank form ready to receive data
    response = render(request, "clicker_app/signup.html",
                      context={"user_form": user_form, "registered": registered})
    return response


def myaccount(request):

    if request.user.is_authenticated:
        purchased_list = OwnsUpgrade.objects.filter(account=request.user.account)
    else:
        return redirect(reverse("clicker_app:login"))
        purchased_list = []

    clicks_per_second = 0
    for item in purchased_list:
        if item.upgrade.auto_click:
            clicks_per_second += item.upgrade.effect*item.quantity

    all_achievements = Achievement.objects.all()

    context_dict = {
        "all_achievements": all_achievements,
        "cps": clicks_per_second,
    }

    response = render(request, "clicker_app/myaccount.html", context=context_dict)
    return response


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse("clicker_app:index"))


class AddPoints(View):
    def post(self, request):
        a = request.POST.get("a", None)
        clicks = request.POST.get("clicks", 1)

        try:
            user_account = Account.objects.get(user__id=a)
        except Exception as e:
            print(e)
            return HttpResponse(-1)

        user_account.points = str(int(user_account.points) + int(clicks))
        user_account.lifetime_points = str(int(user_account.lifetime_points) + int(clicks))
        user_account.save()

        return JsonResponse({
            "points": user_account.points,
            "lifetime_points": user_account.lifetime_points,
        })


class Darkmode(View):
    def post(self, request):
        user_id = request.POST.get("user-id", None)

        try:
            user_account = Account.objects.get(user__id=user_id)
        except Exception as e:
            print(e)
            return HttpResponse(-1)

        user_account.darkmode = not user_account.darkmode
        user_account.save()

        return redirect(request.META.get("HTTP_REFERER"))


class Purchase(View):
    def post(self, request):
        user_id = request.POST.get("user-id", None)
        upgrade = request.POST.get("upgrade", None)

        try:
            user_account = Account.objects.get(user__id=user_id)
            upgrade_instance = Upgrade.objects.get(id=upgrade)
            owns_upgrade = OwnsUpgrade.objects.get_or_create(account=user_account, upgrade=upgrade_instance)[0]
        except Exception:
            return HttpResponse("-1?-1")

        cost_instance = int(owns_upgrade.upgrade.cost * (1.15 ** owns_upgrade.quantity))

        if user_account.points >= cost_instance:
            owns_upgrade.quantity += 1
            user_account.points = user_account.points - cost_instance
            user_account.save()
            owns_upgrade.save()
            cost_instance = int(owns_upgrade.upgrade.cost * (1.15 ** owns_upgrade.quantity))

        owns_upgrade.save()

        return JsonResponse({
            "cost_instance": str(cost_instance),
            "quantity": str(owns_upgrade.quantity),
        })


def upload_image(request):
    if request.method == "POST":
        image_form = ImageUpload(request.POST, request.FILES)
        if image_form.is_valid():
            image_form.save(commit=False)
            account_id = request.POST.get("user-id")
            if "image" in image_form.files.keys():
                new_image = image_form.files["image"]
                user_account = Account.objects.get(user__id=account_id)
                old_image = user_account.image
                if not os.path.samefile(os.path.join(os.getcwd(), "media", str(old_image)), os.path.join(os.getcwd(), "static/images/default-clicker.svg")):
                    old_image.delete()
                # TODO: maybe change image name to account_id new_image.name = account_id
                user_account.image = new_image
                user_account.save()

    return redirect(reverse("clicker_app:myaccount"))


def social_login(request):
    user = request.user
    try:
        Account.objects.get(user=user)
        return redirect(reverse("clicker_app:index"))
    except:  # noqa
        account = Account.objects.create(user=user)
        account.user = user
        account.save()
        return redirect(reverse("clicker_app:index"))
