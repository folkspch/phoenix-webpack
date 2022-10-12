import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phoenix.settings')
import django
django.setup()

import random
import uuid
import datetime
from phoenix.user_app.models import Staff
from faker import Faker
from collections import OrderedDict

locales = OrderedDict([
    ('en-US', 1),
    ('th-TH', 1),
])
fake = Faker(locales)

def gen_user(N):
    for _ in range(N):
        
        if random.choices(fake.locales)[0] == "en_US":
            first_name_set = fake['en-US'].first_name()
            last_name_set = fake['en-US'].last_name()
        else:
            first_name_set = fake['th-TH'].first_name()
            last_name_set = fake['th-TH'].last_name()
        
        uuid_str = fake.bothify(text='########')

        status_set = fake.random_element(
            elements=OrderedDict([
                ("Online", 0.4),
                ("Offline", 0.5),
                ("Terminate", 0.1),
            ])
        ),
        if status_set == ('Terminate',):
            status_set = "Terminate"
        elif status_set == ('Online',):
            status_set = "Online"
        elif status_set == ('Offline',):
            status_set = "Offline"

        created_set = fake.date_time_between(start_date="-2y", end_date="now")
        
        activated_set = fake.date_time_between(start_date=created_set.date(
        ), end_date=created_set.date() + datetime.timedelta(days=10))
        
        terminated_set = fake.date_time_between(start_date=activated_set.date(
        ), end_date="now") if status_set == 'Terminate' else None

        updated_set = fake.date_time_between(start_date=terminated_set.date(), end_date="now") if terminated_set else fake.date_time_between(start_date=activated_set.date(), end_date="now")

        staff = Staff.objects.get_or_create(
            uuid=uuid.uuid5(uuid.NAMESPACE_DNS,uuid_str),
            first_name=first_name_set,
            last_name=last_name_set,
            email=fake.email(),
            mobile_phone=fake['th-TH'].phone_number(),
            username='user' + str(N),
            password=fake.password(length=12),
            national_id=fake.ssn(),
            dob=fake.date_of_birth(),
            role=fake.random_element(
                elements=OrderedDict([
                    ("Guest", 0.5),
                    ("User", 0.2),
                    ("Staff", 0.2),
                    ("Admin", 0.1),
                ])
            ),
            code=fake.bothify(text='####'),
            status=status_set,
            created_at=created_set,
            activated_at=activated_set,
            terminated_at=terminated_set,
            updated_at=updated_set,
        )[0]
        staff.save()

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    gen_user(50)
    print('Populating Complete')
