from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyText

from employee.models import User
from restaurant.models import Item, Menu, Ratings, Restaurant


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = FuzzyText(length=15)
    username = FuzzyText(length=12)


class ItemFactory(DjangoModelFactory):
    class Meta:
        model = Item

    name = FuzzyText(length=15)
    type = FuzzyText(length=15)
    description = FuzzyText(length=50)


class RestaurantFactory(DjangoModelFactory):
    class Meta:
        model = Restaurant

    name = FuzzyText(length=12)
    street = FuzzyText(length=12)
    city = FuzzyText(length=12)
    state = FuzzyText(length=12)
    country = FuzzyText(length=12)


class MenuFactory(DjangoModelFactory):
    class Meta:
        model = Menu

    restaurants = SubFactory(RestaurantFactory)
    day = FuzzyChoice(choices=["MON", "TUE", "WED", "THUR", "FRI"])


class RatingsFactory(DjangoModelFactory):
    class Meta:
        model = Ratings

    # menu = SubFactory(MenuFactory)
    user = SubFactory(UserFactory)
    vote = FuzzyChoice(choices=[-1, 0, 1])
