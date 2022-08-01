from unittest.mock import MagicMock, patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from restaurant.factory_boy import (
    ItemFactory,
    MenuFactory,
    RatingsFactory,
    RestaurantFactory,
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
        assert rating.vote == result_data["vote_value"]

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
