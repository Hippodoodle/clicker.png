import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clicker_png.settings')

import django  # noqa: E402
django.setup()

from clicker_app.models import Achievement, Upgrade  # noqa: E402


def populate():

    achievements = [
        {'name': 'First Achievement',
         'description': 'The first one. Congrats, you made it!'},
        {'name': 'Second Achievement',
         'description': 'The second one.'},
        {'name': 'Welcome!',
         'description': 'You\'ve created an account.'},
        {'name': 'Impossible Achievement',
         'description': 'You shouldn\'t have this.'},
    ]

    upgrades = [
        {'name': 'Extra Cursor',
         'cost': 10,
         'effect': 2,
         'auto_click': False},
        {'name': 'Friendly Bot MkI',
         'cost': 25,
         'effect': 1,
         'auto_click': True},
        {'name': 'Bigger Cursors',
         'cost': 50,
         'effect': 10,
         'auto_click': False},
        {'name': 'Friendly Bot MkII',
         'cost': 100,
         'effect': 5,
         'auto_click': True},
        {'name': 'Hacked Bot',
         'cost': 1000,
         'effect': 100,
         'auto_click': True},
    ]

    for achievement in achievements:
        add_achievement(achievement['name'], achievement['description'])

    for upgrade in upgrades:
        add_upgrade(upgrade['name'], upgrade['cost'],
                    upgrade['effect'], upgrade['auto_click'])

    for a in Achievement.objects.all():
        print(f'- {a}')

    for u in Upgrade.objects.all():
        print(f'- {u}')


def add_achievement(name, description):
    a = Achievement.objects.get_or_create(
        name=name, description=description)[0]
    a.save()
    return a


def add_upgrade(name, cost, effect, auto_click):
    u = Upgrade.objects.get_or_create(
        name=name, cost=cost, effect=effect, auto_click=auto_click)[0]
    u.save()
    return u


if __name__ == '__main__':
    print('Starting Clicker.png population script...')
    populate()
