from unittest.mock import MagicMock, patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from restaurant.factory_boy import RestaurantFactory


class TestRestaurantAPIs(APITestCase):
    """
    Test the Restaurant api
    GET, POST, PUT, PATCH, DELETE
    """

    headers = {"Authorization": "Token token_key"}

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_restaurant_list(self):
        # method to test the getting of restaurnt list
        created_restaurants = [RestaurantFactory() for i in range(3)]
        res = self.client.get(
            reverse("restaurant-list"),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_200_OK
        assert len(result_data) == len(created_restaurants)
        for restaurant, result in zip(created_restaurants, result_data):
            assert str(restaurant.id) == result["id"]
            assert restaurant.name == result["name"]
            assert restaurant.street == result["street"]
            assert restaurant.city == result["city"]
            assert restaurant.state == result["state"]
            assert restaurant.country == result["country"]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_restaurant_creation(self):
        # method to test the creation of restaurnt
        data = {
            "name": "ICH",
            "state": "MP",
            "city": "Indore",
            "country": "India",
            "street": "MG road",
        }
        res = self.client.post(
            reverse("restaurant-list"),
            data=data,
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_201_CREATED
        assert result_data["name"] == data["name"]
        assert result_data["street"] == data["street"]
        assert result_data["city"] == data["city"]
        assert result_data["country"] == data["country"]
        assert result_data["state"] == data["state"]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_restaurant_detail(self):
        # method to test the getting particular restaurnt detail
        restaurant = RestaurantFactory()
        res = self.client.get(
            reverse("restaurant-detail", args=[str(restaurant.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_200_OK
        assert str(restaurant.id) == result_data["id"]
        assert restaurant.name == result_data["name"]
        assert restaurant.street == result_data["street"]
        assert restaurant.city == result_data["city"]
        assert restaurant.state == result_data["state"]
        assert restaurant.country == result_data["country"]
