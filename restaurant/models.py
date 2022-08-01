from django.db import models

from employee.models import AbstructBaseModel, User


class Restaurant(AbstructBaseModel):
    """
    Restaurant model to store fields in database.
    name : Restaurant name
    street : Address of Restaurant
    city : Restaurant city
    state : Restaurant state
    country : Restaurant country
    """

    name = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Item(AbstructBaseModel):
    """
    Menu model to store the items/dishes
    name : Item/Dish name
    type : Item/Dish Type (Chineese,South Indian)
    description : Item/Dish Description
    """

    class ITEM_TYPE:
        CHINEESE = "Chineese"
        SOUTH_INDIAN = "South Indian"

    ITEM_TYPE_CHOICES = [
        (ITEM_TYPE.CHINEESE, "Chineese"),
        (ITEM_TYPE.SOUTH_INDIAN, "South Indian"),
    ]
    name = models.CharField(max_length=70)
    type = models.CharField(max_length=30, choices=ITEM_TYPE_CHOICES)
    description = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name


class Menu(AbstructBaseModel):
    """
    Menu model to link items to restaurant
    restaurant : Restaurant name to link the item
    day : Days ('MON','TUE','WED','THUR','FRI')
    item : many to many field to link item to restaurant menu
    """

    class DAY:
        MON = "MON"
        TUE = "TUE"
        WED = "WED"
        THUR = "THUR"
        FRI = "FRI"

    DAY_CHOICES = [
        (DAY.MON, "Monday"),
        (DAY.TUE, "Tuesday"),
        (DAY.WED, "Wednesday"),
        (DAY.THUR, "Thursday"),
        (DAY.FRI, "Friday"),
    ]

    restaurants = models.ForeignKey(
        Restaurant, related_name="restaurant_menu", on_delete=models.CASCADE
    )
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    item = models.ManyToManyField(Item)

    def __str__(self) -> str:
        return "{}-{}".format(self.restaurants, self.day)


class Ratings(AbstructBaseModel):
    """
    Rating model to link menu to rating
    menu : Restaurant menu which is to be voted
    user : User linked using many to many field
    rating : Rating between 0-10
    timestamp : Todays date time
    """

    VOTE_CHOICES = [(-1, "Dislike"), (0, "Neutral"), (1, "Like")]

    menu = models.ForeignKey(
        Menu, related_name="menu_ratings", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, related_name="user_ratings", on_delete=models.CASCADE
    )
    vote = models.CharField(
        choices=VOTE_CHOICES, max_length=10, default=VOTE_CHOICES[0][1]
    )
    rate = models.JSONField(null=True)
