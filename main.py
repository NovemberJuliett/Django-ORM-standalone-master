import os
import django
from datetime import datetime


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
    for person in not_closed_visits:
        print(person.passcard)
    local_time = localtime()
    entered_at = Visit.objects.filter(entered_at__isnull=False)
    for person in entered_at:
        entered = person.entered_at
        resides = local_time - entered
        # print("Зашёл в хранилище, время по Москве:", local_time)
        # print("Находится в хранилище:", str(resides).split('.')[0])



# print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
