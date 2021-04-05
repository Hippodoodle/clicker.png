import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clicker_png.settings')

import django  # noqa: E402
django.setup()

from clicker_app.models import Achievement, Upgrade  # noqa: E402


def populate():

    achievements = [
        {'name': 'Welcome!',
         'description': 'Congrats, you made it!',
         'condition': 0,
         'current_score_achievement': False},
        {'name': 'Double Digits!',
         'description': 'Get 10 pixels. Buy yourself an upgrade.',
         'condition': 10,
         'current_score_achievement': False},
        {'name': '8-bit Textures',
         'description': 'Own 64 pixels at once. Not enough for a whole minecraft block.',
         'condition': 64,
         'current_score_achievement': True},
        {'name': 'Looking Good!',
         'description': 'Own 384 pixels at once. Enough for a minecraft bloack!',
         'condition': 384,
         'current_score_achievement': True},
        {'name': 'Four Zeroes',
         'description': 'Get 10000 pixels. Moving up in the world.',
         'condition': 10000,
         'current_score_achievement': False},
        {'name': '1080p',
         'description': 'Get 2073600 pixels. Full High Definition Resolution.',
         'condition': 2073600,
         'current_score_achievement': False},
        {'name': '1',
         'description': '1',
         'condition': 42000000000,
         'current_score_achievement': False},
        {'name': '2',
         'description': '2',
         'condition': 999999999999,
         'current_score_achievement': False},
        {'name': '3',
         'description': '3',
         'condition': 999999999999,
         'current_score_achievement': False},
        {'name': '4',
         'description': '4',
         'condition': 999999999999,
         'current_score_achievement': False},
        {'name': '5',
         'description': '5',
         'condition': 999999999999,
         'current_score_achievement': False},
    ]

    upgrades = [
        {'name': 'Extra Cursor',
         'cost': 10,
         'effect': 2,
         'auto_click': False},
        {'name': 'Bigger Cursors',
         'cost': 5000,
         'effect': 10,
         'auto_click': False},
        {'name': 'QHD PNG',
         'cost': 1000000,
         'effect': 200,
         'auto_click': False},
        {'name': 'Gaming Mouse',
         'cost': 50000000000,
         'effect': 2000,
         'auto_click': False},
        {'name': 'Friendly Bot MkI',
         'cost': 15,
         'effect': 1,
         'auto_click': True},
        {'name': 'Pixel Mining Script v1.0',
         'cost': 100,
         'effect': 2,
         'auto_click': True},
        {'name': 'Friendly Bot MkII',
         'cost': 500,
         'effect': 4,
         'auto_click': True},
        {'name': 'Pixel Mining Script v2.0',
         'cost': 3000,
         'effect': 10,
         'auto_click': True},
        {'name': 'Boris the Hacker',
         'cost': 10000,
         'effect': 40,
         'auto_click': True},
        {'name': 'Unstable Bot MkIII',
         'cost': 40000,
         'effect': 100,
         'auto_click': True},
        {'name': 'Download RAM',
         'cost': 200000,
         'effect': 400,
         'auto_click': True},
        {'name': 'Hacked Mining Script v3.0',
         'cost': 1666666,
         'effect': 6666,
         'auto_click': True},
        {'name': 'M.A.R.V.I.N.',
         'cost': 123456789,
         'effect': 98765,
         'auto_click': True},
        {'name': 'Quantum Supercomputer Access',
         'cost': 3999999999,
         'effect': 999999,
         'auto_click': True},
        {'name': 'Alien Tech',
         'cost': 75000000000,
         'effect': 10000000,
         'auto_click': True},
    ]

    for achievement in achievements:
        add_achievement(achievement['name'], achievement['description'],
                        achievement['condition'], achievement['current_score_achievement'])

    for upgrade in upgrades:
        add_upgrade(upgrade['name'], upgrade['cost'], upgrade['effect'], upgrade['auto_click'])

    for a in Achievement.objects.all():
        print(f'- {a}')

    for u in Upgrade.objects.all():
        print(f'- {u}')


def add_achievement(name, description, condition, current_score_achievement):
    a = Achievement.objects.get_or_create(name=name, description=description)[0]
    a.condition = condition
    a.current_score_achievement = current_score_achievement
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
