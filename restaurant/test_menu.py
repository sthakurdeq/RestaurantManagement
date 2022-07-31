from unittest.mock import MagicMock, patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from restaurant.factory_boy import ItemFactory, MenuFactory, RestaurantFactory


class TestMenuAPIs(APITestCase):
    """
    Test the Menu api
    GET, POST, PUT, PATCH, DELETE
    """

    headers = {"Authorization": "Token token_key"}

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_menu_list(self):
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
            reverse("menu-list"),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_200_OK
        for menu_data, result in zip(created_menu, result_data):
            assert str(menu_data.id) == result["id"]
            assert str(menu_data.restaurants_id) == result["restaurants"]
            assert menu_data.day == result["day"]
            item_ids = [item_result["id"] for item_result in result["items"]]
            assert item_ids == [str(a.id) for a in menu_data.item.all()]

    # @patch(
    #     "rest_framework.authtoken.models.Token",
    #     MagicMock(return_value=headers["Authorization"]),
    # )
    # def test_menu_creation(self):
    #     # method to test the creation of menu
    #     data = {
    #         "restaurants": "UUID('986abf1c-a524-4557-897d-d8dbeb3b6af0')",
    #         "day": "MON",
    #         "item": [
    #             {
    #                 'id': "UUID('91d787e4-27bd-4b6a-ac0a-54019d7fad49')",
    #                 'name': 'OQImnsAyWiblokn'
    #             }
    #         ],

    #     }
    #     # restaurant = RestaurantFactory()
    #     # menu = MenuFactory(restaurants=restaurant)
    #     # menu.item.add(ItemFactory())
    #     # breakpoint()
    #     res = self.client.post(
    #         reverse("menu-list"),
    #         data=data,
    #         format="json",
    #         HTTP_AUTHORIZATION="Token token_key",
    #     )
    #     result_data = res.json()
    #     breakpoint()
    #     assert res.status_code == status.HTTP_201_CREATED
    #     assert result_data["restaurants"] == data["restaurants"]
    #     assert result_data["day"] == data["day"]
    #     assert result_data["item"] == data["item"]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_menu_detail(self):
        # method to test the getting prticular of menu
        restaurant = RestaurantFactory()
        menu = MenuFactory(restaurants=restaurant)
        created_item = [ItemFactory() for a in range(3)]
        menu.item.add(created_item[0])
        menu.item.add(created_item[1])
        menu.item.add(created_item[2])
        res = self.client.get(
            reverse("menu-detail", args=[str(menu.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_200_OK
        assert str(menu.id) == result_data["id"]
        assert str(menu.restaurants_id) == result_data["restaurants"]
        assert menu.day == result_data["day"]
        item_ids = [item_result for item_result in result_data["item"]]
        assert item_ids == [str(a.id) for a in menu.item.all()]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_menu_partial_update(self):
        # method to test the partil updation of menu
        restaurant = RestaurantFactory()
        menu = MenuFactory(restaurants=restaurant)
        created_item = [ItemFactory() for a in range(2)]
        menu.item.add(created_item[0])
        menu.item.add(created_item[1])
        res = self.client.patch(
            reverse("menu-detail", args=[str(menu.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_200_OK
        assert str(menu.id) == result_data["id"]
        assert str(menu.restaurants_id) == result_data["restaurants"]
        assert menu.day == result_data["day"]
        item_ids = [item_result for item_result in result_data["item"]]
        assert item_ids == [str(a.id) for a in menu.item.all()]

    # @patch(
    #     "rest_framework.authtoken.models.Token",
    #     MagicMock(return_value=headers["Authorization"]),
    # )
    # def test_menu_update(self):
    #     # method to test the updation of menu
    #     restaurant = RestaurantFactory()
    #     menu = MenuFactory(restaurants=restaurant)
    #     created_item = [ItemFactory() for a in range(2)]
    #     menu.item.add(created_item[0])
    #     menu.item.add(created_item[1])
    #     res = self.client.put(
    #         reverse("menu-detail", args=[str(menu.id)]),
    #         format="json",
    #         HTTP_AUTHORIZATION="Token token_key",
    #     )
    #     result_data = res.json()
    #     assert res.status_code == status.HTTP_200_OK
    #     assert str(menu.id) == result_data["id"]
    #     assert str(menu.restaurants_id) == result_data["restaurants"]
    #     assert menu.day == result_data["day"]
    #     item_ids = [item_result for item_result in result_data["item"]]
    #     assert item_ids == [str(a.id) for a in menu.item.all()]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_menu_delete(self):
        # method to test the deletion of menu
        restaurant = RestaurantFactory()
        menu = MenuFactory(restaurants=restaurant)
        created_item = [ItemFactory() for a in range(2)]
        menu.item.add(created_item[0])
        menu.item.add(created_item[1])
        res = self.client.delete(
            reverse("menu-detail", args=[str(menu.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        assert res.status_code == status.HTTP_204_NO_CONTENT
