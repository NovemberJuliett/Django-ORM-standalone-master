import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    cards = Passcard.objects.all()
    some_name = cards[0]
    owner_name = some_name.owner_name
    passcode = some_name.passcode
    created_at = some_name.created_at
    is_active = some_name.is_active
    # print("owner_name:", owner_name)
    # print("passcode:", passcode)
    # print("created_at:", created_at)
    # print("is_active:", is_active)
    # active_passcards = []
    # for card in cards:
    #     if card.is_active:
    #         active_passcards.append(card)
    active_passcards = Passcard.objects.filter(is_active=True)
    print("Всего пропусков", len(cards))
    print("Активных пропусков", len(active_passcards))


    # print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
