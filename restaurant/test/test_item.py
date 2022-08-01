from unittest.mock import MagicMock, patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from restaurant.factory_boy import ItemFactory


class TestItemAPIs(APITestCase):
    """
    Test the Items api
    GET, POST, PUT, PATCH, DELETE
    """

    headers = {"Authorization": "Token token_key"}

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_item_list(self):
        # method to test the geting list of items
        created_item = [ItemFactory() for i in range(3)]
        res = self.client.get(
            reverse("item-list"),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_200_OK
        assert len(result_data) == len(created_item)
        for item, result in zip(created_item, result_data):
            assert str(item.id) == result["id"]
            assert item.name == result["name"]
            assert item.type == result["type"]
            assert item.description == result["description"]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_item_creation(self):
        # method to test the creation of item
        data = {
            "name": "Idli",
            "type": "Chineese",
            "description": "Very Delicious",
        }
        res = self.client.post(
            reverse("item-list"),
            data=data,
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_201_CREATED
        assert result_data["name"] == data["name"]
        assert result_data["type"] == data["type"]
        assert result_data["description"] == data["description"]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_item_detail(self):
        # method to test the particular item detail
        item = ItemFactory()
        res = self.client.get(
            reverse("item-detail", args=[str(item.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_200_OK
        assert str(item.id) == result_data["id"]
        assert item.name == result_data["name"]
        assert item.type == result_data["type"]
        assert item.description == result_data["description"]
