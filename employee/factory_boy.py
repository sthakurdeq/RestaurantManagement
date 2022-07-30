from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyText

from employee.models import User

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = FuzzyText(length=15)
    username = FuzzyText(length=15)