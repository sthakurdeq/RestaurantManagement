from re import U
from unittest.mock import MagicMock, patch, Mock
from django.test.client import RequestFactory
from django.urls import reverse
from requests import request
from rest_framework import status
from rest_framework.test import APITestCase
from restaurant import views as restautant_views
from restaurant.factory_boy import (
    ItemFactory,
    MenuFactory,
    RatingsFactory,
    RestaurantFactory,
    UserFactory,
)


class TestRatingsAPIs(APITestCase):
    """
    Test the Rating api
    GET, POST, PUT, PATCH, DELETE
    """

    headers = {"Authorization": "Token token_key"}

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_rating_list(self):
        # method to test the getting list of ratings
        created_rating = []
        for j in range(3):
            restaurant = RestaurantFactory()
            menu = MenuFactory(restaurants=restaurant)
            created_item = [ItemFactory() for i in range(3)]
            menu.item.add(created_item[0])
            menu.item.add(created_item[1])
            menu.item.add(created_item[2])
            rating = RatingsFactory(menu=menu)
            created_rating.append(rating)
        res = self.client.get(
            reverse("rating-list"),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_200_OK
        assert len(result_data) == len(created_rating)
        for rating, result in zip(created_rating, result_data):
            assert str(rating.id) == result["id"]
            assert str(rating.menu.id) == result["menu"]
            assert str(rating.user).strip() == result["user"].strip()
            assert rating.vote == result["vote"]

    # @patch(
    #     "rest_framework.authtoken.models.Token",
    #     MagicMock(return_value=headers["Authorization"]),
    # )
    # def test_rating_creation(self):
    #     # method to test the creation of rating
    #     data = {
    #         "menu": "f27aca4f-f80c-4640-b3a7-b6a7ef5dd9cb",
    #         "user": "e0e0fa8e-a1a4-41e1-9e70-950749f23d23",
    #         "vote": "-1",
    #     }
    #     res = self.client.post(
    #         reverse("rating-list"),
    #         data=data,
    #         format="json",
    #         HTTP_AUTHORIZATION="Token token_key",
    #     )
    #     result_data = res.json()
    #     assert res.status_code == status.HTTP_201_CREATED
    #     assert result_data["menu"] == data["menu"]
    #     assert result_data["user"] == data["user"]
    #     assert result_data["vote"] == data["vote"]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_rating_detail(self):
        # method to test the particular rating detail
        restaurant = RestaurantFactory()
        menu = MenuFactory(restaurants=restaurant)
        created_item = [ItemFactory() for i in range(3)]
        menu.item.add(created_item[0])
        menu.item.add(created_item[1])
        menu.item.add(created_item[2])
        rating = RatingsFactory(menu=menu)
        res = self.client.get(
            reverse("rating-detail", args=[str(rating.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_200_OK
        assert str(rating.id) == result_data["id"]
        assert str(rating.menu.id) == result_data["menu"]
        assert rating.vote == result_data["vote"]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_rating_partial_update(self):
        # method to test the partial updation of rating
        restaurant = RestaurantFactory()
        menu = MenuFactory(restaurants=restaurant)
        created_item = [ItemFactory() for i in range(3)]
        menu.item.add(created_item[0])
        menu.item.add(created_item[1])
        menu.item.add(created_item[2])
        rating = RatingsFactory(menu=menu)
        res = self.client.patch(
            reverse("rating-detail", args=[str(rating.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        expected_result = {"message": "Update function is not offered in this path."}
        assert res.status_code == status.HTTP_403_FORBIDDEN
        assert expected_result == result_data

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_rating_update(self):
        # method to test the updation of rating
        restaurant = RestaurantFactory()
        menu = MenuFactory(restaurants=restaurant)
        created_item = [ItemFactory() for i in range(3)]
        menu.item.add(created_item[0])
        menu.item.add(created_item[1])
        menu.item.add(created_item[2])
        rating = RatingsFactory(menu=menu)
        res = self.client.put(
            reverse("rating-detail", args=[str(rating.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        expected_result = {"message": "Update function is not offered in this path."}
        result_data = res.json()
        assert res.status_code == status.HTTP_403_FORBIDDEN
        assert expected_result == result_data

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_rating_delete(self):
        # method to test the deletion of rating
        restaurant = RestaurantFactory()
        menu = MenuFactory(restaurants=restaurant)
        created_item = [ItemFactory() for i in range(3)]
        menu.item.add(created_item[0])
        menu.item.add(created_item[1])
        menu.item.add(created_item[2])
        rating = RatingsFactory(menu=menu)
        expected_result = {"message": "Delete function is not offered in this path."}
        res = self.client.delete(
            reverse("rating-detail", args=[str(rating.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_403_FORBIDDEN
        assert expected_result == result_data

    @patch(
    "rest_framework.authtoken.models.Token",
    MagicMock(return_value=headers["Authorization"]),
    )
    def test_today_menu_list(self):
        # method to test the getting list of menus
        created_menu = []
        for j in range(3):
            restaurant = RestaurantFactory()
            menu = MenuFactory(restaurants=restaurant)
            created_item = [ItemFactory() for i in range(3)]
            menu.item.add(created_item[0])
            menu.item.add(created_item[1])
            menu.item.add(created_item[2])
            created_menu.append(menu)
        res = self.client.get(
            reverse("today_menu-list"),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        res = self.client.get(
            reverse("today_menu-list"),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        assert res.status_code == status.HTTP_200_OK
        for menu_data, result in zip(created_menu, result_data):
            assert str(menu_data.id) == result["id"]
            assert str(menu_data.restaurants_id) == result["restaurants"]
            assert menu_data.day == result["day"]
            item_ids = [item_result["id"] for item_result in result["items"]]
            assert item_ids == [str(a.id) for a in menu_data.item.all()]

