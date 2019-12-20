from factory import SubFactory, django, fuzzy
from api import models
from faker import Faker
import uuid
from nextmotion.settings import AUTH_USER_MODEL
from django.contrib.auth.models import User
from datetime import datetime
from pytz import utc


fake = Faker()


class UserFactory(django.DjangoModelFactory):
    
    class Meta:	
    	model = User

    email = fake.ascii_email()
    username = fake.name()
    password = fake.first_name()

    is_superuser = True
    is_staff = True
    is_active = True


class FactoryInvitation(django.DjangoModelFactory):

	class Meta:
		model = models.Invitation

	id = uuid.uuid4()
	created_time = datetime.now(utc)
	email = fake.ascii_email()
	creator = SubFactory(UserFactory)	