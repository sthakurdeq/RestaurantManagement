from unittest.mock import MagicMock, patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from restaurant.factory_boy import RatingsFactory


class TestRatingsAPIs(APITestCase):
    headers = {"Authorization": "Token token_key"}

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_rating_list(self):
        created_rating = [RatingsFactory() for i in range(3)]
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
            assert rating.menu == result["menu"]
            assert rating.user == result["user"]
            assert rating.vote == result["vote"]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_rating_creation(self):
        data = {
            "menu": "f27aca4f-f80c-4640-b3a7-b6a7ef5dd9cb",
            "user": "e0e0fa8e-a1a4-41e1-9e70-950749f23d23",
            "vote": "-1",
        }
        res = self.client.post(
            reverse("rating-list"),
            data=data,
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_201_CREATED
        assert result_data["menu"] == data["menu"]
        assert result_data["user"] == data["user"]
        assert result_data["vote"] == data["vote"]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_rating_detail(self):
        rating = RatingsFactory()
        res = self.client.get(
            reverse("rating-detail", args=[str(rating.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_200_OK
        assert str(rating.id) == result_data["id"]
        assert rating.menu == result_data["menu"]
        assert rating.user == result_data["user"]
        assert rating.vote == result_data["vote"]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_item_partial_update(self):
        rating = RatingsFactory()
        res = self.client.patch(
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
    def test_item_update(self):
        rating = RatingsFactory()
        res = self.client.put(
            reverse("item-detail", args=[str(rating.id)]),
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
        # breakpoint()
        rating = RatingsFactory()
        expected_result = {"message": "Delete function is not offered in this path."}
        res = self.client.delete(
            reverse("item-detail", args=[str(rating.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_403_FORBIDDEN
        assert expected_result == result_data
