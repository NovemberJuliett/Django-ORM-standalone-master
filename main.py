import os
import django
import datetime


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard
from datacenter.models import Visit  # noqa: E402
from django.utils.timezone import localtime


if __name__ == '__main__':
    cards = Passcard.objects.all()
    some_name = cards[0]
    owner_name = some_name.owner_name
    passcode = some_name.passcode
    created_at = some_name.created_at
    is_active = some_name.is_active

    active_passcards = Passcard.objects.filter(is_active=True)
    # print("Всего пропусков", len(cards))
    # print("Активных пропусков", len(active_passcards))

    not_closed_visits = Visit.objects.filter(leaved_at__isnull=True)
    # print(not_closed_visits)
    local_time = localtime()
    entered_at = Visit.objects.filter(entered_at__isnull=False)
    print(entered_at)
    for person in entered_at:
        print("Зашёл в хранилище, время по Москве:", local_time)
        delta = local_time - entered_at
        print("Находится в хранилище:", delta.hour)


    # print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
