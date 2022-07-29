from django.db import models
from employee.models import AbstructBaseModel
# Create your models here.


class Restaurant(AbstructBaseModel):
    '''
    Restaurant model to store fields in database.
    name : Restaurant name
    street : Address of Restaurant
    city : Restaurant city
    state : Restaurant state
    country : Restaurant country
    '''
    name=models.CharField(max_length=50)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)

class Item(AbstructBaseModel):
    '''
    Menu model to store the items/dishes
    name : Item/Dish name
    type : Item/Dish Type (Chineese,South Indian)
    description : Item/Dish Description
    '''
    class ITEM_TYPE:
        CHINEESE = "Chineese"
        SOUTH_INDIAN = "South Indian"
    
    ITEM_TYPE_CHOICES = [
        (ITEM_TYPE.CHINEESE, "Chineese"),
        (ITEM_TYPE.SOUTH_INDIAN, "South Indian"),
    ]
    name=models.CharField(max_length=70)
    type=models.CharField(max_length=30,choices=ITEM_TYPE_CHOICES)
    description=models.CharField(max_length=150)

class Menu(AbstructBaseModel):
    '''
    Menu model to link items to restaurant
    restaurant : Restaurant name to link the item
    day : Days ('MON','TUE','WED','THUR','FRI')
    item : many to many field to link item to restaurant menu
    '''
    DAY=(('MON','Monday'),('TUE','Tuesday'),('WED','Wednesday'),('THUR','Thursday'),('FRI','Friday'))
    VOTE=((-1,-1),(0,0),(1,1))
    restaurant_name=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    day=models.CharField(max_length=10,choices=DAY)
    vote=models.IntegerField(choices=VOTE)
    item=models.ManyToManyField(Item)

