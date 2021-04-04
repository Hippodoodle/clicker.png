from django.http import HttpResponse
from django.shortcuts import render, redirect
from clicker_app.forms import UserForm
from django.contrib.auth import authenticate, default_app_config, logout, login  # noqa: F401
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from clicker_app.models import Achievement, Upgrade, Account, OwnsUpgrade  # noqa: F401
from django.views import View


def index(request):

    upgrades_list = Upgrade.objects.order_by('cost')
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
    leaderboard_list = Account.objects.order_by('-lifetime_points')[:10]
   
    ranking_list = Account.objects.order_by('-lifetime_points')


    context_dict = {}
    context_dict['leaderboard'] = leaderboard_list
    context_dict['upgrade_table'] = upgrade_table_dict
    context_dict['purchased_list'] = purchased_list

    context_dict['ranking_list'] = ranking_list
    response = render(request, 'clicker_app/index.html', context=context_dict)
    return response


def about(request):
    response = render(request, 'clicker_app/about.html')
    return response


def tutorial(request):
    response = render(request, 'clicker_app/tutorial.html')
    return response


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('clicker_app:index'))
            else:
                return HttpResponse("Your account is disabled")
        else:
            print("Invalid login details, please try again")
            return HttpResponse("Invalid login details supplied")
    else:
        response = render(request, 'clicker_app/login.html')
        return response


def signup(request):
    registered = False  # registration unsuccessful initially
    if request.method == 'POST':  # if form is post, attempt to process
        user_form = UserForm(request.POST)  # take information from form
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            account = Account.objects.create(user=user)
            account.user = user
            account.save()

            registered = True  # save to databbase, registration successful
        else:
            print(user_form.errors)  # invalid attempt
    else:
        user_form = UserForm()  # give blank form ready to receive data
    response = render(request, 'clicker_app/signup.html',
                      context={'user_form': user_form, 'registered': registered})
    return response


def myaccount(request):
    response = render(request, 'clicker_app/myaccount.html')
    return response


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('clicker_app:index'))


class AddPoints(View):
    def post(self, request):
        a = request.POST.get('a', None)

        try:
            user_account = Account.objects.get(user__id=a)
        except Exception as e:
            print(e)
            return HttpResponse(-1)

        user_account.points = str(int(user_account.points) + 1)
        user_account.lifetime_points = str(int(user_account.lifetime_points) + 1)
        user_account.save()

        return HttpResponse(user_account.points)


class Darkmode(View):
    def post(self, request):
        user_id = request.POST.get('user-id', None)

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
        user_id = request.POST.get('user-id', None)
        upgrade = request.POST.get('upgrade', None)

        try:
            user_account = Account.objects.get(user__id=user_id)
            upgrade_instance = Upgrade.objects.get(id=upgrade)
            owns_upgrade = OwnsUpgrade.objects.get_or_create(account=user_account, upgrade=upgrade_instance)[0]
        except Exception:
            return HttpResponse("-1?-1")

        owns_upgrade.quantity += 1
        owns_upgrade.save()

        cost_instance = int(owns_upgrade.upgrade.cost*owns_upgrade.quantity*0.5)

        print(str(cost_instance)+"?"+str(owns_upgrade.quantity))

        return HttpResponse(str(cost_instance)+"?"+str(owns_upgrade.quantity))
