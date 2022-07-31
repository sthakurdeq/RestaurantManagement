from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyText

from employee.models import User
from restaurant.models import Item, Menu, Ratings, Restaurant


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = FuzzyText(length=15)


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

    restaurant = SubFactory(RestaurantFactory)
    item = SubFactory(ItemFactory)
    user = SubFactory(UserFactory)
    vote = True


class RatingsFactory(DjangoModelFactory):
    VOTE_CHOICES = [(-1, "Dislike"), (0, "Neutral"), (1, "Like")]

    class Meta:
        model = Ratings

    menu = SubFactory(MenuFactory)
    user = SubFactory(UserFactory)
    vote = FuzzyChoice(VOTE_CHOICES)
