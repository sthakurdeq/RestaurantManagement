from unittest.mock import MagicMock, patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from restaurant.factory_boy import ItemFactory


class TestItemAPIs(APITestCase):
    headers = {"Authorization": "Token token_key"}

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_item_list(self):
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

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_item_partial_update(self):
        item = ItemFactory()
        res = self.client.patch(
            reverse("item-detail", args=[str(item.id)]),
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
    def test_item_update(self):
        item = ItemFactory()
        res = self.client.put(
            reverse("item-detail", args=[str(item.id)]),
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
    def test_item_delete(self):
        item = ItemFactory()
        expected_result = {"message": "Delete function is not offered in this path."}
        res = self.client.delete(
            reverse("item-detail", args=[str(item.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_403_FORBIDDEN
        assert expected_result == result_data
